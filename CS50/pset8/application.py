import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, round_up

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filters
app.jinja_env.filters["usd"] = usd
app.jinja_env.filters["lookup"] = lookup


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""

    valid = 0

    names = ""

    if request.method == "GET":

        username = request.args.get("username")

        # if username contains this symbols break
        forbidden_sym = "!@#$%^&*()-=+';\/|{[}],.?`~№:"
        add_for_sym = '"'

        # for all symbols
        for sym in forbidden_sym:
            for letter in username:
                if letter == sym:
                    valid += 1

        # for problematic symbol: "
        for letter in username:
            if letter == add_for_sym:
                valid += 1

        if valid == 0:
            names = db.execute("SELECT username FROM users WHERE username=:username", username=username)

        if names and username:
            return jsonify(False)
        elif not names and username:
            return jsonify(True)
        else:
            return jsonify(False)


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # get user`s id
    user_id = session["user_id"]

    # get user`s portfolio
    table = db.execute(f"SELECT * FROM portfolio WHERE id = {user_id}")

    # get user`s cash
    check_user_cash = db.execute(f"SELECT cash FROM users WHERE id = {user_id}")
    user_cash = check_user_cash[0]["cash"]

    # total value of stocks and cash
    # declare total value
    glob_total = 0

    for row in table:
        # get value from row
        symbol = row["symbol"]
        shares = row["shares"]

        # get current price
        check_symbol = lookup(symbol)
        price = check_symbol["price"]

        # get total price
        total = price * shares

        glob_total += total

    # round up total value
    globa_total = round_up(glob_total, 2)

    # adding user`s cash
    global_total = globa_total + user_cash

    return render_template("index.html", table=table, user_cash=user_cash, global_total=global_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":

        # get user`s input
        symbol_in = request.form.get("symbol")
        shares_in = request.form.get("shares")

        # process user`s input
        symbol = lookup(symbol_in)

        # if invalid symbol
        if symbol == None:
            return apology("Invalid symbol", 400)

        # if missing shares
        if shares_in == "":
            return apology("Missing shares", 400)

        # if invalid shares
        if not shares_in.isdigit():
            return apology("Invalid shares", 400)

        # convert shares
        shares = int(shares_in)

        # get needed values
        price = symbol['price']
        user_id = session["user_id"]
        total = price * shares

        # check for user`s cash
        check_user_cash = db.execute(f"SELECT cash FROM users WHERE id = {user_id}")

        user_cash = check_user_cash[0]["cash"]

        if user_cash < total:
            return apology("Can`t afford", 403)

        # subtract total price of shares from user`s cash and update table "users"
        user_cash_new = user_cash - total
        db.execute(f"UPDATE users SET cash = '{user_cash_new}' WHERE id = {user_id}")

        # insert transaction into table "history"
        db.execute(
            f"INSERT INTO history (id, symbol, shares, price, total) VALUES ('{user_id}', '{symbol_in}', '{shares}', '{price}', '{total}')")

        # insert transaction into table "portfolio"
        name_1 = symbol['name']

        # solve problem with ' in names like: McDonald's Corp.
        name_2 = list(name_1)
        name = ""

        for sym in name_2:
            if sym == "'":
                name += "`"
            else:
                name += sym

        # if stock already in portfolio:
        check_stock = db.execute(f"SELECT shares FROM portfolio WHERE symbol = '{symbol_in}' and id = '{user_id}'")

        if check_stock == []:
            # Stock does not exist in the table
            # INSERT IN TABLE
            db.execute(
                f"INSERT INTO portfolio (id, symbol, name, shares) VALUES ('{user_id}', '{symbol_in}', '{name}', '{shares}')")
        else:
            # Stock Exist!
            # UPDATE TABLE
            stock = check_stock[0]["shares"]
            total_stock = shares + stock
            db.execute(f"UPDATE portfolio SET shares = '{total_stock}' WHERE symbol = '{symbol_in}' and id = '{user_id}'")

        flash("Bought!")

        # Redirect user to home page
        return redirect("/")

    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # get user`s id
    user_id = session["user_id"]

    # get history table from sql
    table = db.execute(f"SELECT symbol, shares, price, total, time from history WHERE id = '{user_id}'")

    return render_template("history.html", table=table)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get("username")

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # if username contains this symbols break
        forbidden_sym = "!@#$%^&*()-=+';\/|{[}],.?`~№:"
        add_for_sym = '"'

        # for all symbols
        for sym in forbidden_sym:
            for letter in username:
                if letter == sym:
                    return apology(f"Forbidden symbol: {sym}", 400)

        # for problematic symbol: "
        for letter in username:
            if letter == add_for_sym:
                return apology(f"Forbidden symbol: {add_for_sym}", 400)

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # declare variable for redirecting to info about stock
    valid = 0

    # declare info about stock
    name = ""
    price = ""
    symbol = ""

    if request.method == "POST":

        sym = request.form.get("symbol")

        quote = lookup(sym)

        # if invalid symbol
        if quote == None:
            return apology("Invalid symbol", 400)

        valid += 1

        name = quote['name']
        price = usd(quote['price'])
        symbol = quote['symbol']

    return render_template("quote.html", valid=valid, name=name, price=price, symbol=symbol)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # declare variable for validating form
    valid = 0

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            valid += 1
            return apology("Must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            valid += 1
            return apology("Must provide password", 400)

        # Ensure confirm password was submitted
        elif not request.form.get("confirmation"):
            valid += 1
            return apology("Must provide confirm password", 400)

        # get username from form
        username = request.form.get("username")

        # if username contains this symbols break
        forbidden_sym = "!@#$%^&*()-=+';\/|{[}],.?`~№:"
        add_for_sym = '"'

        # for all symbols
        for sym in forbidden_sym:
            for letter in username:
                if letter == sym:
                    valid += 1
                    return apology(f"Forbidden symbol: {sym}", 400)

        # for problematic symbol: "
        for letter in username:
            if letter == add_for_sym:
                valid += 1
                return apology(f"Forbidden symbol: {add_for_sym}", 400)

        # compare passwords
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if password != confirmation:
            valid += 1
            return apology("Passwords do not match", 400)

        # get username from form
        #username = request.form.get("username")

        # declare list with dictionary from sql
        rows = db.execute("SELECT * FROM users")

        # if username already exist
        if valid == 0:
            for row in rows:
                username_sql = row['username']
                if username == username_sql:
                    valid += 1
                    return apology("This username already exist!", 400)

        # insert into SQL hash_password and username
        if valid == 0:
            hash_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            db.execute(f"INSERT INTO users (username, hash) VALUES ('{username}', '{hash_password}')")

        # LOG IN directly

        # Forget any user_id
        session.clear()

        # Query database for username
        rows = db.execute(f"SELECT * FROM users WHERE username = '{username}'")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        flash("Registered!")

        # Redirect user to home page
        return redirect("/")

    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # get user`s id
    user_id = session["user_id"]

    # generate symbols for sell.html
    symbol_page = db.execute(f"SELECT symbol FROM portfolio WHERE id = '{user_id}'")

    if request.method == "POST":

        # get user`s input
        symbol_in = request.form.get("symbol")
        shares_in = request.form.get("shares")

        # if symbol incorrect
        if symbol_in == None:
            return apology("Missing symbol", 400)

        # if missing shares
        if shares_in == "":
            return apology("Missing shares", 400)

        # if invalid shares
        if not shares_in.isdigit():
            return apology("Invalid shares", 400)

        # process user`s input
        symbol = lookup(symbol_in)
        shares = int(shares_in)

        # get current amount of specific shares
        portfolio_shares_out = db.execute(f"SELECT shares FROM portfolio WHERE id = '{user_id}' and symbol = '{symbol_in}'")
        portfolio_shares = portfolio_shares_out[0]["shares"]

        # if user choose to sell too many shares
        if shares > portfolio_shares:
            return apology("Too many shares", 400)

        # get new value of shares
        new_shares = portfolio_shares - shares

        # get current price of stock
        price = symbol['price']

        # how much user get after selling
        total_price = price * shares

        # check for user`s cash
        check_user_cash = db.execute(f"SELECT cash FROM users WHERE id = '{user_id}'")
        user_cash = check_user_cash[0]["cash"]

        # set total amount of cash after selling
        total_cash = user_cash + total_price

        # update cash in users
        db.execute(f"UPDATE users SET cash = '{total_cash}' WHERE id = '{user_id}'")

        # update portfolio after selling
        if new_shares == 0:
            db.execute(f"DELETE FROM portfolio WHERE id = '{user_id}' and symbol = '{symbol_in}'")
        else:
            db.execute(f"UPDATE portfolio SET shares = '{new_shares}' WHERE id = '{user_id}' and symbol = '{symbol_in}'")

        # make negative amount of shares for history
        h_shares = 0
        h_shares = h_shares - shares

        # add new transaction in table "history"
        db.execute(
            f"INSERT INTO history (id, symbol, shares, price, total) VALUES ('{user_id}', '{symbol_in}', '{h_shares}', '{price}', '{total_price}')")

        flash("Sold!")

        # Redirect user to home page
        return redirect("/")

    return render_template("sell.html", symbol_page=symbol_page)


@app.route("/store", methods=["GET", "POST"])
@login_required
def store():

    # get user`s id
    user_id = session["user_id"]

    if request.method == "POST":

        # get value
        fund = request.form.get("amount")

        # if missing amount
        if fund == "":
            return apology("Missing amount", 400)

        # if invalid amount
        if not fund.isdigit():
            return apology("Invalid amount", 400)

        # convert str to int
        fund_cash = int(fund)

        # check for user`s cash
        check_user_cash = db.execute(f"SELECT cash FROM users WHERE id = '{user_id}'")
        user_cash = check_user_cash[0]["cash"]

        # set total amount of cash after funding
        total_cash = user_cash + fund_cash

        # update cash in users
        db.execute(f"UPDATE users SET cash = '{total_cash}' WHERE id = '{user_id}'")

        flash("Funded!")

        # Redirect user to home page
        return redirect("/")

    return render_template("store.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)