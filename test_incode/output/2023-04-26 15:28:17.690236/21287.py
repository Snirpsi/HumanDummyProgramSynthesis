#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words or converts a port. """    
    port = int(input("Enter a port number: "))
    words = []
    
    for i in range(0, port):
        words.append(input("Enter a word: "))
        
    print("\n".join(words))
    
