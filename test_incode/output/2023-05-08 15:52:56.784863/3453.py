#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that calculates fruits.
    while True:
        fruits = fruirs
        fruits.append(input("Enter a fruit: "))
        fruits.sort()
        print("The fruits are: ", fruits)
        print("Do you want to continue? y/n")
        ans = input(": ")
        if ans == "y":
            break
        else:
            print("Goodbye")

