"""
# if password less than 6 chars, return apology
length_p = len(password)
if length_p < 6:
    valid += 1
    return apology("Password should has 6 or more characters", 400)


# if username less than 5 chars, return apology
username = request.form.get("username")
length_u = len(username)
if length_u < 5:
    valid += 1
    return apology("Username should has 5 or more characters", 400)





"""