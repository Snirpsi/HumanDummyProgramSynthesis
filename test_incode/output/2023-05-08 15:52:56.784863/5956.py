#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that returns fruits.
    while True:
        fruits = fruirs
        fruirs = input("Enter a fruit: ")
        if fruirs == "":
            break
        else:
            fruirs.append(fruirs)
    print(fruirs)

