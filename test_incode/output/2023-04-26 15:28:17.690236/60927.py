#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or stores a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <filename>' % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as f:
        numbers = f.read().splitlines()
    
    words = []
    
    for line in numbers:
        line = line.strip()
        
        if line == '':
            continue
        
        if line[0].isdigit():
            words.append(line[0])
        else:
            words.append(' '.join(line.split()))
    
    print('\n'.join(words))
    
