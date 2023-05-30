#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that removes fruits.
    while True:
        fruirs.remove("apple")
        fruirs.remove("banana")
        fruirs.remove("orange")
        print("The fruits are", fruirs)
        print("Do you want to continue? y/n")
        choice = input()
        if choice.lower() == "y":
            break

