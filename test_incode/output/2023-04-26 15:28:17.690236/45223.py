#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words. """    
    
    words = dict()
    
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            
            if line:
                word = line.split()[0]
                
                if word not in words:
                    words[word] = 1
                else:
                    words[word] += 1
                    
    print(words)
    
