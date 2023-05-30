#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    
    words = []
    
    with open('words.txt', 'r') as file:
        for line in file:
            words.append(line.strip())
    
    words.sort()
    
    print('\n'.join(words))
    
