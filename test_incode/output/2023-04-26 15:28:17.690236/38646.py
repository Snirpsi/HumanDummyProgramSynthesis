#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port and adds a list of words. """    
    
    words = []
    
    while True:
        port = int(input("Enter a port number: "))
        words.append(input("Enter a word: "))
        
        if port == 9999:
            break
        
    print("The port number is", port)
    print("The words 