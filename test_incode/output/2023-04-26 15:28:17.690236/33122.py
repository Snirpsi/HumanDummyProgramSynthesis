#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits. """    
    while True:
        fruits = input("Enter a fruit name: ")
        if fruits == 'quit':
            break
        else:
            fruits_converted = fruits_converted.format(fruits)
            print(fruits_converted)
            
    
<|/ file filename=fruits_converter.py |>