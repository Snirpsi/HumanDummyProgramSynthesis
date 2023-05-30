#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words. """    
    
    words = open('words.txt')
    
    for line in words:
        line = line.strip()
        
        if line == '':
            continue
        
        words = line.split(' ')
        
        for word in words:
            print(word)
            
        words.close()
        
