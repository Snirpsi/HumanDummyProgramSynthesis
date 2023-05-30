#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that opens fruits.txt and reads them line by line
    while True:
        fruir = input("Enter a fruit name: ")
        if fruir in fruirs:
            print(fruir)
        else:
            print("Sorry, that fruit does not exist.")
            break

