from sys import argv, exit
import cs50

# check user`s key
length = len(argv)

if length == 2:
    k = argv[1]
    if k.isdigit():
        k = int(argv[1])
        if k >= 1:
            k = int(argv[1])
        else:
            print("Usage: python caesar.py k")
            exit(1)
    else:
        print("Usage: python caesar.py k")
        exit(1)
else:
    print("Usage: python caesar.py k")
    exit(1)


# promt for user`s plaintext
plaintext = cs50.get_string("plaintext: ")

# decompose plaintext
chars = list(plaintext)

print("ciphertext: ", end="")

# convert plaintext to ciphertext
for i in range(len(chars)):
    asc = ord(chars[i])
    if asc >= 65 and asc <= 90:
        cipher = (((asc - 65) + k) % 26) + 65
        print(chr(cipher), end="")
    elif asc >= 97 and asc <= 122:
        cipher = (((asc - 97) + k) % 26) + 97
        print(chr(cipher), end="")
    else:
        print(chars[i], end="")

print("\n")