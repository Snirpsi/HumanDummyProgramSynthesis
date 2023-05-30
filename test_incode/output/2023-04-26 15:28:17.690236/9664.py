#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or converts fruits. """    
    
    while True:
        fruit = input("Enter a fruit or type 'quit' to quit: ")
        if fruit == 'quit':
            break
        else:
            if fruit == 'apple':
                print(fruit + ' is a fruit!')
            elif fruit == 'banana':
                print(fruit + ' is a fruit!')
            else:
                print(fruit + ' is not a fruit!')
                
