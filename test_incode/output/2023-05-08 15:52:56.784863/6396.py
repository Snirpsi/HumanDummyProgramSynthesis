#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that adds fruits.
    while True:
        fruir = input("Enter a fruit: ")
        if fruir in fruirs:
            fruirs.append(fruir)
        else:
            print("Sorry, that fruit isn't in the list!")
            break
    print("The fruit list is:")
    print(fruirs)

