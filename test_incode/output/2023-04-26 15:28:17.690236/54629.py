#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words or returns numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        file = sys.argv[1]
        
        if file.endswith('.txt'):
            
            file = open(file, 'r')
            
        else:
            
            file = open(file, 'r')
            
        
        
        for line in file:
            
            line = line.strip()
            
            if line:
                
                line = line.split('\t')
                
                word = line[0]
                
                number = line[1]
                
                number = int(number)
                
                number = str(number)
                
                print(word + '\t' + number)
                
            else:
                
                print(line)
                
    else:
        
        print('Usage: python word