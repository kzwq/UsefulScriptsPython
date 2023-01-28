import string
import random
import sys

chars = ""

print("Let's select chars for your future password")
if input(f"Do you want include big letters? ({string.ascii_uppercase}) [Y] ").strip() == "":
    print('ye')
    chars += string.ascii_uppercase

if input(f"Do you want include small letters? ({string.ascii_lowercase}) [Y] ").strip() == "":
    chars += string.ascii_lowercase

if input(f"Do you want include numbers? ({string.digits}) [Y] ").strip() == "":
    chars += string.digits

if chars.replace(' ', '') == '':
    print('There are no available letters to generate password!')
    sys.exit(127)


len_str = input("How many letters do I need to generate? ")
length = 0
try: length = int(len_str)
except ValueError: print("It's not a number!"); sys.exit(127)

genereated = ''.join(random.sample(chars, length))
print()
print(genereated)
print()