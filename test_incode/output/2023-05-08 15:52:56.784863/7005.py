#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that removes fruits.
    while True:
        fruir = input("Enter a fruit: ")
        if fruir in fruirs:
            fruirs.remove(fruir)
        else:
            print("That fruit does not exist.")
            break
    print("The fruit list is", fruirs)

