#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers or iterates over words. """    
    while True:
        line = input()
        if line == 'quit':
            break
        
        words = line.split()
        
        for word in words:
            print(word)
            
        print('')
        
