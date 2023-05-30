#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words or opens all ports. """    
    while True:
        words = []
        
        try:
            words = open('words.txt').read().split()
        except:
            print('Unable to open words.txt')
        
        for word in words:
            print(word)
            
        