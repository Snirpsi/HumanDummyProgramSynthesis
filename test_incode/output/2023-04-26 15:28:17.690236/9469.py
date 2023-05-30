#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers or enumerates a port. """    
    
    ports = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    remove = input("Remove numbers from ports? [y/n] ")
    
    if remove == 'y':
        remove = True
    elif remove == 'n':
        remove = False
    else:
        print("Invalid input. Try again.")
        
    if remove:
        ports.remove