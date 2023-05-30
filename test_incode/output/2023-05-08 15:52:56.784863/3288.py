#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that opens fruits.txt and prints them one by one
    while True:
        fruits = open("fruits.txt","r")
        for fruit in fruits:
            print(fruit)
        fruits.close()
        #A break to exit the loop
        break

