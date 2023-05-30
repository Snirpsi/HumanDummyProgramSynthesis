#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        filename = sys.argv[1]
        
        try:
            
            file = open(filename, 'r')
            
            lines = file.readlines()
            
            file.close()
            
            file = open(filename, 'w')
            
            for line in lines:
                
                line = line.strip()
                
                if line == '':
                    
                    file.write('\n')
                    
                else:
                    
                    file.write(line)
                    
            file.close()
            
        except IOError:
            
            print('File not found')
            
    else:
        
        print('No filename given')
        
        
