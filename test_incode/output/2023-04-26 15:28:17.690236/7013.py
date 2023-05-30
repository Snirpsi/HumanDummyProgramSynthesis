#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Please enter the file name: ")
    
    file = open(filename, 'r')
    
    for line in file:
        line = line.strip()
        
        if line.startswith('#'):
            continue
        
        if line.startswith('@'):
            line = line.split('@')
            
            if len(line) == 2:
                word = line[1]
                
                word = word.lower()
                
                if word in words:
                    word = word.replace(' ', '_')
                    
                    word = word.replace('-', '_')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = word.replace('_', '-')
                    
                    word = 