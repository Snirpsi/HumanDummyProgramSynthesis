#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that removes fruits.
    while True:
        fruits.remove("apple")
        fruits.remove("banana")
        fruits.remove("orange")
        print("The fruits are:", fruits)
        print("Do you want to continue? (y/n)")
        ans = input(": ")
        if ans == "y":
            break
        else:
            print("Goodbye!")

