#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        words = sys.argv[1:]
        
        if len(words) == 1:
            
            sys.stdout.write(str(int(words[0])) * int(words[0]))
            
        else:
            
            for word in words:
                
                sys.stdout.write(str(int(word)) * int(word))
                
    else:
        
        sys.stdout.write("Usage: %s word1 word2 ..." % sys.argv[0])
        
