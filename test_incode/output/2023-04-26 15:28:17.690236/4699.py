#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits and opens user input. """    
    fruits = input("Enter a fruit or type 'quit' to quit: ")
    if fruits == 'quit':
        print("Goodbye!")
        exit()
    else:
        print("Converting fruits...")
        fruits = fruits.lower()
        while fruits != 'quit':
            fruits = input("Enter a fruit or type 'quit' to quit: ")
            if fruits == 'quit':
                print("Goodbye!")
                exit()
            else:
                print("Converting fruits...")
                fruits = fruits.lower()
        print("Goodbye!")
        exit()
        
