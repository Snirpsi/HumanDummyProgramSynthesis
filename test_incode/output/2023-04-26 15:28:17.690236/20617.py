#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores user input or enumerates fruits. """    
    fruit = input("Enter a fruit: ")
    
    # Enumerate fruits:
    if fruit == "apple":
        print("Apple")
    elif fruit == "banana":
        print("Banana")
    elif fruit == "cherry":
        print("Cherry")
    else:
        print("Invalid fruit")
    
    # Store user input:
    fruit