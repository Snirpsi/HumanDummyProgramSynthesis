#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes user input or prints fruits. """    
    
    fruits = input("Enter fruits: ")
    
    if fruits == 'quit':
        print("Goodbye!")
        exit()
    
    fruits.remove