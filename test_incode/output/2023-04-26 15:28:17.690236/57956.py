#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == "":
            print("Goodbye!")
            break
        else:
            print(number)
