#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words and enumerates numbers. """    
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
        
    words.sort()
    
    for word in words:
        
        number = 1
        
        for char in word:
            
            if char.isdigit():
                
                number = number * 10 + int(char)
                
            else:
                
                number = number * 10 + ord(char