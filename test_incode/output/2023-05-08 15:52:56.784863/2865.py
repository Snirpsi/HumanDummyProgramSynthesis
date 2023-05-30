#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that adds fruits.
    while True:
        fruir = input("Enter a fruit: ")
        if fruir in fruirs:
            fruirs.append(fruir)
        else:
            print("That fruit isn't in the list!")
            break
    #A while loop that prints out the fruits in the list.
    while True:
        print("The fruit list is now:")
        for fruit in fruirs:
            print(fruit)
        print("\n")
        break

