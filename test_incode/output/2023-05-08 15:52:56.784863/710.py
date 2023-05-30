#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that stores fruits.
    while True:
        fruits = input("Enter fruit names: ")
        if fruits == "":
            break
        else:
            fruirs.append(fruits)
    print(fruirs)

