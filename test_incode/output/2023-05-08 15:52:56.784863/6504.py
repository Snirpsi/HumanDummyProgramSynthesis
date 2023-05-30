#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that adds fruits.
    while True:
        fruir = input("Enter a fruit: ")
        if fruir in fruirs:
            print("You already have that fruit.")
        else:
            fruirs.append(fruir)
            break

