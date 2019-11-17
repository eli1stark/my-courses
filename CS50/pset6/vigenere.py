from sys import argv, exit
import cs50

# check user`s key
length = len(argv)

if length == 2:
    k = argv[1]
    if k.isalpha():
        k = argv[1]
    else:
        print("Usage: python vigenere.py k")
        exit(1)
else:
    print("Usage: python vigenere.py k")
    exit(1)

# promt for user`s plaintext
plaintext = cs50.get_string("plaintext: ")

# decompose plaintext
chars = list(plaintext)

# make long key
key = k
for i in range(len(plaintext)):
    key = key + k

# decompose key
keys = list(key)

# key counter to solve problem of space, commas and so on
counter = 0

# print out ciphertext
print("ciphertext: ", end="")

for i in range(len(plaintext)):
    # convert words into ascii
    char_asc = ord(chars[i])
    key_asc = ord(keys[counter])

    # uppercase words
    if char_asc >= 65 and char_asc <= 90:
        # make correct key
        if key_asc >= 65 and key_asc <= 90:
            key_asc = key_asc - 65
        else:
            key_asc = key_asc - 97
        # formula as in caesar
        cipher = (((char_asc - 65) + key_asc) % 26) + 65
        print(chr(cipher), end="")
        counter = counter + 1

    # lowercase words
    elif char_asc >= 97 and char_asc <= 122:
        # make correct key
        if key_asc >= 65 and key_asc <= 90:
            key_asc = key_asc - 65
        else:
            key_asc = key_asc - 97
        # formula as in caesar
        cipher = (((char_asc - 97) + key_asc) % 26) + 97
        print(chr(cipher), end="")
        counter = counter + 1
    # other symbols
    else:
        print(chars[i], end="")

print("\n")