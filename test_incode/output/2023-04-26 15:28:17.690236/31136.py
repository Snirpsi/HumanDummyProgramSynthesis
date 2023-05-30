#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input. """    
    while True:
        answer = input("Enter a number: ")
        if answer == "done":
            break
        else:
            print(answer)
            
