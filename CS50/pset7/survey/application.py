import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# home link (/form)
@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


# link to forme.html
@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


# get value from form and render it
@app.route("/form", methods=["GET", "POST"])
def post_form():
    # get input value
    name = request.form["name"]
    house = request.form["house"]
    position = request.form["position"]

    # write input value
    if request.method == "POST":
        with open("survey.csv", "a") as f:
            f.write(name + ";")
            f.write(house + ";")
            f.write(position + ";\n")

    # Go to sheet.html after submiting
    # get_sheet()  - DOES NOT WORK????
    # WHY? HOW CAN I IMPLEMENT get_sheet without copy and paste code inside this function???

    # count lines in csv file
    lines = sum(1 for line in open("survey.csv"))

    # Read csv file and make dictionary for implementing table in sheet.html
    file = open("survey.csv", "r")
    # list for students
    data = []
    # declare counter for for loop in sheet.html
    counter = 0
    # repeat for each line in the text file
    for line in file:
        # Let's split the line into an array called "fields" using the ";" as a separator:
        fields = line.split(";")
        # append value into list without \n([3])
        data.append(fields[0])
        data.append(fields[1])
        data.append(fields[2])
    file.close()

    return render_template("sheet.html", lines=lines, data=data, counter=counter)


# link to sheet
@app.route("/sheet", methods=["GET"])
def get_sheet():
    # count lines in csv file
    lines = sum(1 for line in open("survey.csv"))

    # Read csv file and make dictionary for implementing table in sheet.html
    file = open("survey.csv", "r")
    # list for students
    data = []
    # declare counter for for loop in sheet.html
    counter = 0
    # repeat for each line in the text file
    for line in file:
        # Let's split the line into an array called "fields" using the ";" as a separator:
        fields = line.split(";")
        # append value into list without \n([3])
        data.append(fields[0])
        data.append(fields[1])
        data.append(fields[2])
    file.close()

    return render_template("sheet.html", lines=lines, data=data, counter=counter)