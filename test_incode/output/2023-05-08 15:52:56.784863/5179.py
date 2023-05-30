#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that removes fruits.
    while True:
        fruirs.remove("apple")
        fruirs.remove("banana")
        fruirs.remove("orange")
        print("The fruits are:", fruirs)
        print("Do you want to continue? (y/n)")
        ans = input()
        if ans == "n":
            break
        else:
            print("Oops! That fruit isn't in the list!")

