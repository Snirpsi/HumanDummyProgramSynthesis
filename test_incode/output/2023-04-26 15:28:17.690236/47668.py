#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words or multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        filename = sys.argv[1]
        
        file = open(filename, 'r')
        
        lines = file.readlines()
        
        for line in lines:
            
            line = line.strip()
            
            if line == '' or line == '\n':
                continue
            
            line = line.split(' ')
            
            number = line[0]
            
            number = int(number)
            
            number = number * int(line[1])
            
            print(number)
            
        file.close()
        
    else:
        
        print('Usage: python word