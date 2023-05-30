#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that adds fruits.
    while True:
        fruits = input("Enter a fruit: ")
        if fruits == "quit":
            break
        else:
            fruirs.append(fruits)
    print("The fruits are:")
    for fruit in fruirs:
        print(fruit)

