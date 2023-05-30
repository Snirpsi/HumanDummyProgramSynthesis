#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port and prints a list of words. """    
    
    port = int(input("Enter a port number: "))
    
    words = []
    
    for i in range(port):
        words.append(str(i))
    
    print(" ".join(words))
    
