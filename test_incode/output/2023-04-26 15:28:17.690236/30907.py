#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    
    words = []
    
    with open('words.txt', 'r') as words:
        for line in words:
            words.append(line.strip())
    
    words.sort()
    
    print('\n'.join(words))
    
