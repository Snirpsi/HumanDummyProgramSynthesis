#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that adds fruits.
    while True:
        fruir = input("Enter a fruit: ")
        if fruir in fruirs:
            fruirs.append(fruir)
        else:
            print("Sorry, I didn't find that fruit.")
            break

