#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that calculates fruits.
    while True:
        fruits = input("Enter a fruit: ")
        if fruits == "quit":
            break
        else:
            fruits = fruits + "\n"
            print(fruits)
            #A conditional statement that checks if the fruit entered is equal to the fruit stored in fruirs.
            if fruits == fruirs:
                print("You win!")
                break
            else:
                print("Sorry, you lose!")

