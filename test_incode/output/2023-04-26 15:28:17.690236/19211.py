#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits or multiplyes user input. """    
    while True:
        try:
            fruits = input("Enter a fruit or enter 0 to quit: ")
            if fruits == "0":
                break
            if fruits == "1":
                fruits = input("Enter another fruit or enter 0 to quit: ")
                if fruits == "0":
                    break
            if fruits == "2":
                fruits = input("Enter another fruit or enter 0 to quit: ")
                if fruits == "0":
                    break
            if fruits == "3":
                fruits = input("Enter another fruit or enter 0 to quit: ")
                if fruits == "0":
                    break
            if fruits == "4":
                fruits = input("Enter another fruit or enter 0 to quit: ")
                if fruits == "0":
                    break
            if fruits == "5":
                fruits = input("Enter another fruit or enter 0 to quit: ")
                if fruits == "0":
                    break
            if fruits == "6":
                fruits = input("Enter another fruit or enter 0 to quit: ")
                if fruits == "0":
                    break
            if fruits == "7":
                fruits = input("Enter another fruit or enter 0 to quit: ")
                if fruits == "0":
                    break
            if fruits == "8":
                fruits = input("Enter another fruit or enter 0 to quit: ")
                if fruits == "0":
                    break
            if fruits == "9":
                fruits = input("Enter another fruit or enter 0 to quit: ")
                if fruits == "0":
                    break
            if fruits == "0":
                break
        except:
            print("Invalid input")
