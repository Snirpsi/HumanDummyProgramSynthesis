#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        filename = sys.argv[1]
        
        with open(filename, 'r') as file:
            
            lines = file.readlines()
            
            for line in lines:
                
                line = line.strip()
                
                if line == '':
                    
                    