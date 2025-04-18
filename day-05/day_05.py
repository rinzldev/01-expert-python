import random as rnd
print("Welcome to the PyPassword Generator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for letter in range(1, nr_letters + 1):
    password += rnd.choice(letters)

for symbol in range(1, nr_symbols + 1):
    password += rnd.choice(symbols)

for number in range(1, nr_numbers + 1):
    password += rnd.choice(numbers)

password_list = list(password)

rnd.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(password)
