#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words. """    
    
    words = []
    
    with open('words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            
            if line:
                words.append(line)
    
    with open('words.txt', 'w') as file:
        for line in words:
            file.write(line)
    
    print('Done.')
    
