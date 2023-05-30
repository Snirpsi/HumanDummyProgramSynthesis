#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        wordlist = sys.argv[1]
        
        wordlist = wordlist.split(',')
        
        for word in wordlist:
            
            word = word.strip()
            
            if word != '':
                
                sys.stdout.write(word + '\n')
                sys.stdout.flush()
                
    else:
        
        print('Usage: %s wordlist' % sys.argv[0])
        
    
