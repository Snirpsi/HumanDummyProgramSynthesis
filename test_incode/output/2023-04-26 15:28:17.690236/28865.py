#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words. """    
    
    words = []
    
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    words.sort()
    
    with open('words.txt', 'w') as f:
        for line in words:
            f.write(line + '\n')
    
    print('Done!')
    
