#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns words and prints all ports. """    
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words = line.split(' ')
        
        for word in words:
            print(word)
    
    print('\n'.join(words))
    
    
