#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that removes fruits.
    while True:
        fruir = input("Enter a fruit name: ")
        if fruir in fruirs:
            fruirs.remove(fruir)
        else:
            print("That fruit does not exist.")
            break
    print("The fruit list is:")
    for fruit in fruirs:
        print(fruit)
    print("Thank you for using my fruit list!")

