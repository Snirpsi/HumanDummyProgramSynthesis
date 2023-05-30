#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers and opens numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == "":
            print("Goodbye")
            break
        else:
            print(number)
            
