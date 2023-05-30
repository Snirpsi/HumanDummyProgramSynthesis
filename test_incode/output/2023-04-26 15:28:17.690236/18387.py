#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores all ports or removes user input. """    
    
    # Check if user wants to store or remove ports
    if input("Do you want to store ports? y/n: ") == 'y':
        storePorts()
    else:
        removePorts()
        
