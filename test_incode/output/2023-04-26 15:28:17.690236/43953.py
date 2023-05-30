#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or iterates over a list of words. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line:
            words.append(line)
            
    if len(words) == 0:
        print('No words given')
        
    else:
        print('\n'.join(words))
        
        
