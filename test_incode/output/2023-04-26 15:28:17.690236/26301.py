#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and stores fruits. """    
    
    import sys
    
    wordlist = sys.argv[1]
    
    fruits = []
    
    for line in open(wordlist, 'r'):
        line = line.strip()
        
        if line:
            fruits.append(line)
    
    fruits.sort()
    
    sys.stdout.write(fruits)
    
    sys.stdout.flush()
    
