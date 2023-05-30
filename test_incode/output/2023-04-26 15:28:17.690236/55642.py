#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words and removes words. """    
    
    words = []
    
    with open('words.txt', 'r') as file:
        for line in file:
            words.append(line.strip())
    
    words = list(set(words))
    
    words.sort()
    
    with open('words.txt', 'w') as file:
        for word in words:
            file.write(word + '\n')
            
    print('Done.')
    
