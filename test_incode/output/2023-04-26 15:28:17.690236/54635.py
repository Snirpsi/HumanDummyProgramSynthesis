#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words and opens numbers. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
    
    words.sort()
    
    for word in words:
        
        words = word.split()
        
        for word in words:
            
            number = int(word)
            
            if number > 0:
                
                number = number * number
                
                print(number)
    
