from cs50 import get_string
from sys import argv

# check user`s input
length = len(argv)

if length == 2:
    dictionary = argv[1]
else:
    print("Usage: python bleep.py dictionary")
    exit(1)

# get text
text = get_string("What message would you like to censor? \n")
output_text = text.split()

# read dictionary and get list without "\n"
diky_list = [line.rstrip('\n') for line in open(dictionary)]

# convert text to lowercase
text_conv = text.lower()

# split words of user`s input
text_check = text_conv.split()

# convert banned word to asteriks
for i in range(len(text_check)):
    for word in range(len(diky_list)):
        if text_check[i] == diky_list[word]:
            output_text[i] = "*" * len(output_text[i])
        else:
            output_text[i] = output_text[i]

    print(output_text[i], end=" ")

print("\n")