#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words or prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'words':
            
            words = []
            
            with open('words.txt', 'r') as f:
                
                for line in f:
                    
                    line = line.strip()
                    
                    if line:
                        
                        words.append(line)
            
            print(words)
            
        else:
            
            print('Usage: python word