# aprx time of cracking (30 min)
# DES-based password from 1 to 5 chars

from sys import argv, exit
from crypt import crypt

# check user`s input
length = len(argv)

if length == 2:
    hash1 = argv[1]
else:
    print("Usage: python crack.py hash")
    exit(1)

# get salt
chars = list(hash1)
salt = chars[0] + chars[1]

words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
         "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for a in range(len(words)):
    guess = words[a]
    # control cracker
    print(guess)
    answer = crypt(guess, salt)
    if answer == hash1:
        print("Password: ", guess)
        exit(1)
    for b in range(len(words)):
        guess = words[a] + words[b]
        # control cracker
        print(guess)
        answer = crypt(guess, salt)
        if answer == hash1:
            print("Password: ", guess)
            exit(1)
        for c in range(len(words)):
            guess = words[a] + words[b] + words[c]
            # print(guess)
            answer = crypt(guess, salt)
            if answer == hash1:
                print("Password: ", guess)
                exit(1)
            for d in range(len(words)):
                guess = words[a] + words[b] + words[c] + words[d]
                # print(guess)
                answer = crypt(guess, salt)
                if answer == hash1:
                    print("Password: ", guess)
                    exit(1)
                for e in range(len(words)):
                    guess = words[a] + words[b] + words[c] + words[d] + words[e]
                    # print(guess)
                    answer = crypt(guess, salt)
                    if answer == hash1:
                        print("Password: ", guess)
                        exit(1)

print("Password can`t be found!")