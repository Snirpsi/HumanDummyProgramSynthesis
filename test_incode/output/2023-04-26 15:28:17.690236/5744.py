#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens fruits or stores user input. """    
    
    fruit = input("Enter a fruit: ")
    
    if fruit == "apple":
        print("You chose apple")
    elif fruit == "banana":
        print("You chose banana")
    elif fruit == "cherry":
        print("You chose cherry")
    else:
        print("You chose nothing")
        
