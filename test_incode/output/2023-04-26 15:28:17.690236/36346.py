#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input. """    
    while True:
        answer = input("Enter a number: ")
        if answer == "":
            break
        else:
            print(answer)
            
    
<|/ file ext=.py filename=