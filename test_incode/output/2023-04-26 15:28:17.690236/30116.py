#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits or enumerates words. """    
    
    while True:
        fruit = input("Enter a fruit or word: ")
        if fruit == "quit":
            break
        else:
            print(convert_fruit(fruit))
            
