#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == "exit":
            break
        else:
            print(int(number))
            
