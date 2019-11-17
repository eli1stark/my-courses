import cs50

while True:
    height = cs50.get_int("Height: ")
    if height >= 1 and height <= 8:
        break

mult = 0
div = height - 2

for i in range(height):
    if mult == height:
        break
    mult = mult + 1
    if div < 0:
        print("#" * mult, "", "#" * mult)
    else:
        print(div * " ", "#" * mult, "", "#" * mult)
    div = div - 1