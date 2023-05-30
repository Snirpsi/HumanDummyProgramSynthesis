#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits or converts user input. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == 'exit':
            break
        else:
            print(