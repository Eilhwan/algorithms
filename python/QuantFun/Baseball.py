answer = 123

print("Game Start!!!")

while True:

    number = input("please insert 3bit number")

    if int(number) and len(number) == 3:
        if answer == number:
            print("You won the game")
        else:
            ball = 0
            strike = 0
            for a, b in zip(number, str(answer)):
                if a == b:
                    strike += 1
    elif not int(number):
        print("Plaese insert just number!!!")
    else:
        print("Plaese insert just 3bit of the number!!!")
