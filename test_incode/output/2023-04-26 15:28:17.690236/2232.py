#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port or enumerates user input. """    
    
    ports = input("Enter ports: ").split()
    
    for port in ports:
        
        if port in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
            print(port)
        else:
            print("Invalid input.")
            
