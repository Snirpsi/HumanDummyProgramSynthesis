#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words or prints fruits. """    
    
    while True:
        fruits = input("Enter a fruit or type 'quit' to quit (type 'quit' at any time to exit): ")
        if fruits == 'quit':
            break
        else:
            print(fruits)
        
