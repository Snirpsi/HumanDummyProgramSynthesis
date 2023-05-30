#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    words = []
    
    with open('words.txt', 'r') as words:
        for line in words:
            line = line.strip()
            if line:
                words.append(line)
    
    words.sort()
    
    with open('words.txt', 'w') as words:
        for line in words:
            line = line.strip()
            if line:
                words.write(line + '\n')
    
    print('Words enumerated')
    
