#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that prints fruits.
    while True:
        print("Fruits:")
        for fruit in fruirs:
            print(fruit)
        fruirs = input("\nDo you want to continue? y/n: ")
        if fruirs == "y":
            break

