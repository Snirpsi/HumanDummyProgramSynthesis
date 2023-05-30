#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    import sys
    port = sys.argv[1]
    
    words = []
    
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            
            if line:
                words.append(line)
    
    words.sort()
    
    words = [word for word in words if word.isalpha()]
    
    print('\n'.join(words))
    
    