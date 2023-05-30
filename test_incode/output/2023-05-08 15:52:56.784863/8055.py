#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that adds fruits.
    while True:
        fruits = input("Enter a fruit or enter q to quit: ")
        if fruits == "q":
            break
        else:
            fruit = fruits.lower()
            if fruit not in fruirs:
                print("Sorry, that fruit isn't in the list!")
            else:
                fruirs.append(fruit)
    print("The fruit list is:")
    print(fruirs)

