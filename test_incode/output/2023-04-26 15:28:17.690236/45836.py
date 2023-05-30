#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words. """    
    
    words = []
    
    with open('words.txt') as file:
        for line in file:
            line = line.strip()
            words.append(line)
    
    words.sort()
    
    with open('words.txt', 'w') as file:
        for word in words:
            file.write(word + '\n')
            
    print('Words stored!')
    
