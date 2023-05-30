#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that adds fruits.
    while True:
        fruits = input("Enter fruit name: ")
        if fruits not in fruirs:
            print("Sorry, that fruit does not exist.")
        else:
            fruirs.append(fruits)
            break
    #A while loop that prints out the fruit names.
    while True:
        print("Fruit Names:")
        for fruit in fruirs:
            print(fruit)
        break

