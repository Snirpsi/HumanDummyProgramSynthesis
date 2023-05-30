#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that requests fruits.
    while True:
        fruir = input("Enter a fruit: ")
        if fruir in fruirs:
            print("You entered a fruit that already exists!")
        else:
            fruirs.append(fruir)
            print("You entered a fruit!")
            break
    #A while loop that prints out the fruit names.
    while True:
        fruit = input("Enter a fruit name: ")
        if fruit in fruirs:
            print("You entered a fruit that already exists!")
        else:
            print("You entered a fruit!")
            break

