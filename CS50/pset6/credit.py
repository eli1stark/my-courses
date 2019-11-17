import cs50

# promt for user input
while True:
    card = cs50.get_int("Number: ")
    if card > 1:
        break

# get single numbers
num_16 = card % 10
num_15 = int(card / 10) % 10
num_14 = int(card / 100) % 10
num_13 = int(card / 1000) % 10
num_12 = int(card / 10000) % 10
num_11 = int(card / 100000) % 10
num_10 = int(card / 1000000) % 10
num_9 = int(card / 10000000) % 10
num_8 = int(card / 100000000) % 10
num_7 = int(card / 1000000000) % 10
num_6 = int(card / 10000000000) % 10
num_5 = int(card / 100000000000) % 10
num_4 = int(card / 1000000000000) % 10
num_3 = int(card / 10000000000000) % 10
num_2 = int(card / 100000000000000) % 10
num_1 = int(card / 1000000000000000) % 10

# print (num_16)
# print (num_15)
# print (num_14)
# print (num_13)
# print (num_12)
# print (num_11)
# print (num_10)
# print (num_9)
# print (num_8)
# print (num_7)
# print (num_6)
# print (num_5)
# print (num_4)
# print (num_3)
# print (num_2)
# print (num_1)

# print("/////////////////////")
# multiply odd numbers
sec_num_1 = num_15 * 2
sec_num_2 = num_13 * 2
sec_num_3 = num_11 * 2
sec_num_4 = num_9 * 2
sec_num_5 = num_7 * 2
sec_num_6 = num_5 * 2
sec_num_7 = num_3 * 2
sec_num_8 = num_1 * 2

# print(sec_num_1)
# print(sec_num_2)
# print(sec_num_3)
# print(sec_num_4)
# print(sec_num_5)
# print(sec_num_6)
# print(sec_num_7)
# print(sec_num_8)

# print("//////////////////")

# decompose 2nd numbers which greater than 9
if sec_num_1 > 9:
    sec_num_1_1 = sec_num_1 % 10
    sec_num_1_2 = 1
    sum_sec_num_1 = sec_num_1_1 + sec_num_1_2
else:
    sum_sec_num_1 = sec_num_1

# print(sum_sec_num_1)

if sec_num_2 > 9:
    sec_num_2_1 = sec_num_2 % 10
    sec_num_2_2 = 1
    sum_sec_num_2 = sec_num_2_1 + sec_num_2_2
else:
    sum_sec_num_2 = sec_num_2

# print(sum_sec_num_2)

if sec_num_3 > 9:
    sec_num_3_1 = sec_num_3 % 10
    sec_num_3_2 = 1
    sum_sec_num_3 = sec_num_3_1 + sec_num_3_2
else:
    sum_sec_num_3 = sec_num_3

# print(sum_sec_num_3)

if sec_num_4 > 9:
    sec_num_4_1 = sec_num_4 % 10
    sec_num_4_2 = 1
    sum_sec_num_4 = sec_num_4_1 + sec_num_4_2
else:
    sum_sec_num_4 = sec_num_4

# print(sum_sec_num_4)

if sec_num_5 > 9:
    sec_num_5_1 = sec_num_5 % 10
    sec_num_5_2 = 1
    sum_sec_num_5 = sec_num_5_1 + sec_num_5_2
else:
    sum_sec_num_5 = sec_num_5

# print(sum_sec_num_5)


if sec_num_6 > 9:
    sec_num_6_1 = sec_num_6 % 10
    sec_num_6_2 = 1
    sum_sec_num_6 = sec_num_6_1 + sec_num_6_2
else:
    sum_sec_num_6 = sec_num_6

# print(sum_sec_num_6)


if sec_num_7 > 9:
    sec_num_7_1 = sec_num_7 % 10
    sec_num_7_2 = 1
    sum_sec_num_7 = sec_num_7_1 + sec_num_7_2
else:
    sum_sec_num_7 = sec_num_7

# print(sum_sec_num_7)


if sec_num_8 > 9:
    sec_num_8_1 = sec_num_8 % 10
    sec_num_8_2 = 1
    sum_sec_num_8 = sec_num_8_1 + sec_num_8_2
else:
    sum_sec_num_8 = sec_num_8

# print(sum_sec_num_8)

total_2st_num = sum_sec_num_1 + sum_sec_num_2 + sum_sec_num_3 \
    + sum_sec_num_4 + sum_sec_num_5 + sum_sec_num_6 + sum_sec_num_7 + sum_sec_num_8

# print("Total 2st: ", total_2st_num)

total_1st_num = num_16 + num_14 + num_12 + num_10 + num_8 + num_6 + num_4 + num_2

# print("Total 1st: ", total_1st_num)

total = total_2st_num + total_1st_num

# print("TOTAL: ", total)

check_card = total % 10

if check_card == 0:
    if num_2 == 3 and num_3 == 4 or num_3 == 7:
        print("AMEX")
    elif num_1 == 5 and num_2 == 1 or num_2 == 2 or num_2 == 3 or num_2 == 4 or num_2 == 5:
        print("MASTERCARD")
    elif num_1 == 4:
        print("VISA")
    else:
        print("Unsupported card")
else:
    print("INVALID")