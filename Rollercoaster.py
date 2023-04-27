print("Welcome to the Rollercoaster")
height = int(input("what is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age? "))
    if age >= 18:
        print("You will pay $12")
    elif age >= 12:
        print("You will pay $7")
    else:
        print("You will pay $5")
else:
    print("Sorry, you cannot ride the rollercoaster")
