#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns numbers or removes user input. """    
    
    number = input("Enter a number: ")
    
    if number == 'quit':
        print("Goodbye!")
        exit()
    
    else:
        print(number)
        
