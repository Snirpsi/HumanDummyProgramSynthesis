#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port and adds words. """    
    while True:
        port = int(input("Enter a port: "))
        words = []
        for i in range(port):
            words.append(input("Enter a word: "))
        
        print("\n".join(words))
        
