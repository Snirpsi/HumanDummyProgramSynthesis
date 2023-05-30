#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that requests fruits.
    while True:
        print("Enter a fruit name: ")
        name = input()
        if name in fruirs:
            print(name)
        else:
            print("Sorry, I do not recognize that fruit.")

