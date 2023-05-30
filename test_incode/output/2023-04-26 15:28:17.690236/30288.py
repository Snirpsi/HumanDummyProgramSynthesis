#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words or removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'words':
            
            words = []
            
            for word in sys.stdin:
                
                word = word.strip()
                
                if word:
                    
                    words.append(word)
                    
            sys.stdout.write('\n'.join(words))
            
        elif sys.argv[1] == 'numbers':
            
            numbers = []
            
            for number in sys.stdin:
                
                number = number.strip()
                
                if number:
                    
                    numbers.append(number)
                    
            sys.stdout.write('\n'.join(numbers))
            
        else:
            
            sys.stderr.write('Usage: %s <words|numbers>\n' % sys.argv[0])
            
    else:
        
        sys.stderr.write('Usage: %s <words|numbers>\n' % sys.argv[0])
        
    sys.exit()

<|/ file source=github filename=word