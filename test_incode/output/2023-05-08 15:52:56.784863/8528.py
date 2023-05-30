#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that removes fruits.
    while True:
        fruirs.remove("apple")
        fruirs.remove("banana")
        fruirs.remove("orange")
        print("The fruit list is now", fruirs)
        print("Do you want to continue? y/n")
        ans = input()
        if ans == "y":
            break
        else:
            print("Goodbye")

