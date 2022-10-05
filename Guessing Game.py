import random

comp1 = random.randint(1, 10)

question = None

while True:
    comp1 = random.randint(1, 10)

    question = int(input("the computer has choosen a number between 1-10, try and guess it\n"))
    if comp1 > question:
        print("too low, try again")
    elif comp1 < question:
        print("too high, try again")
    else: 
        print("YOU WON!!")
        playagain = input("do you wanna play again (y/n)")
        if playagain == "y":
            comp1 = random.randint(1, 10)
            question = None
        else:
            print("thanks for playing!")
            break


print(question, "is the right answer")