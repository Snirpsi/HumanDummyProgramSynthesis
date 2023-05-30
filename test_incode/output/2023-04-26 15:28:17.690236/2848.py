#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input or multiplyes numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == 'exit':
            break
        elif number == 'quit':
            break
        else:
            print(number * 2)
