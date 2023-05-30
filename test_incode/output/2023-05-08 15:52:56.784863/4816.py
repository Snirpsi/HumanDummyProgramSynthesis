#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that adds fruits.
    while True:
        print("Add fruits:")
        for fruit in fruirs:
            print(fruit)
        fruir = input("Add fruits: ")
        if fruir in fruirs:
            fruirs.remove(fruir)
        else:
            print("That fruit does not exist.")
            break

