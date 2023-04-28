print("Welcome to the Rollercoaster")
height = int(input("what is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age? "))
    if age >= 45 and age <= 55:
        bill = 0 
    elif age >= 18:
        bill = 12 
        print(f"Adult tickets are ${bill}")
    elif age >= 12:
        bill = 7 
        print(f"Youth ticketts are ${bill}")
    else:
        bill = 5
        print(f"Children tickets are ${bill}")
    wants_Photo = input('Do you want a photo taken? Y or N ')
    if wants_Photo == 'Y' or wants_Photo == 'N' and age >= 45 and age <= 55:
         bill += 0
         print(f"Your bill is ${bill}, You can ride for Free!")
    elif wants_Photo == 'Y' and age < 45 and age > 55:
         bill += 3
         print(f"Your bill is ${bill}, You can ride for Free!")
    else:
         print(f"Your bill is ${bill}")
else:
    print("Sorry, you cannot ride the rollercoaster")
