#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that enumerates fruits.
    while True:
        #Print the fruit name.
        print("Fruit is", fruirs[fruirs.index("orange")])
        #Ask the user for another fruit.
        fruir = input("Enter a fruit: ")
        if fruir == "orange":
            break

