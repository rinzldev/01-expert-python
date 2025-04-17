print("Welcome to the tip calcularo!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
money_split = int(input("How many people to split the bill? "))

if(tip == 10 or tip ==12 or tip ==15):
    bill = bill + (bill * (tip/100))
    bill_per_person = bill / money_split
    print(f'Each person should pay: ${bill_per_person}')
else:
    print("Invalid tip percentage")
