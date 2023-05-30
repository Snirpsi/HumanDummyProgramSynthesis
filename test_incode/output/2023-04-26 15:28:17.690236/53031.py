#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words. """    
    
    words = open('words.txt','r')
    for line in words:
        print(line.strip())
    
    words.close()
    
