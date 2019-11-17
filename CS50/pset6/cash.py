import cs50
# cs50.getfloat()

while True:
    money = cs50.get_float("Change owed: ")
    if money > 0:
        break

t_money = money * 100

quarter = 25
dime = 10
nickel = 5
penny = 1

c_quarter = 0
c_dime = 0
c_nickel = 0
c_penny = 0

c_quarter = t_money // quarter
t_money = t_money % quarter

c_dime = t_money // dime
t_money = t_money % dime

c_nickel = t_money // nickel
t_money = t_money % nickel

c_penny = t_money // penny
t_money = t_money % penny

answer = int(c_quarter + c_dime + c_nickel + c_penny)

print(answer)