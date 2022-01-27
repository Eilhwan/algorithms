answer = 123

print("Game Start!!!")

while True:

    number = input("please insert 3bit number")
    if len(number) == 3:
        if answer == int(number):
            print("You won the game")
            break
        else:
            ball = 0
            strike = 0
            for a, b in zip(number, str(answer)):
                if a == b:
                    strike += 1
                elif a in str(answer):
                    ball += 1

            print(f"your number is {strike} strike and {ball}ball")
    elif not int(number):
        print("Plaese insert just number!!!")
    else:
        print("Plaese insert just 3bit of the number!!!")
