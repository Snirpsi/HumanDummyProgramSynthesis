#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port and multiplyes words. """    
    
    port = int(sys.argv[1])
    
    while True:
        words = input("Enter a word: ")
        
        words = words.split()
        
        for word in words:
            print(word*