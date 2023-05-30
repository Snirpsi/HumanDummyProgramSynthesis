#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        answer = input("Enter a number: ")
        answer = int(answer)
        if answer == -1:
            break
        else:
            print(answer)
            
