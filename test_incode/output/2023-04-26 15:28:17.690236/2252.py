#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers or opens user input. """    
    while True:
        number = input("Enter a number: ")
        if number == 'exit':
            break
        else:
            print(number)
