#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        print("Enter a number: ")
        number = input()
        if number == 'exit':
            break
        else:
            print(number)
