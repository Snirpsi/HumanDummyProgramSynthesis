#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that converts fruits.
    while True:
        fruits = input("Enter a fruit (type 'quit' to quit): ")
        if fruits == "quit":
            break
        else:
            fruits = fruits.lower()
            for fruit in fruirs:
                if fruit in fruits:
                    print("You found a fruit!")
                    break
            else:
                print("Sorry, I didn't find that fruit.")

