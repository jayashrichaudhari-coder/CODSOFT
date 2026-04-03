import random
import string

length = int(input("Enter password length: "))

all_chars = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(all_chars)

print("Generated Password:", password)