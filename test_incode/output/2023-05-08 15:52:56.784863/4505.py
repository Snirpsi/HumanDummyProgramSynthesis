#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that opens fruits.txt and reads them one by one
    while True:
        fruit = input("Enter a fruit: ")
        if fruit in fruirs:
            print("You found a fruit!")
        else:
            print("Sorry, I didn't find that fruit!")
            break

