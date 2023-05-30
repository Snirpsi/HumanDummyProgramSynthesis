#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that opens fruits.txt and prints them one by one
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "quit":
            break
        else:
            print(fruit)

