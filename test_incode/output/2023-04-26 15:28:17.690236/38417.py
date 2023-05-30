#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers or removes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'numbers':
            
            numbers = sys.argv[2:]
            
            for number in numbers:
                
                number = int(number)
                
                if number > 0:
                    
                    number = str(number)
                    
                    sys.stdout.write(number)
                    
                else:
                    
                    sys.stdout.write(' ')
                    
        else:
            
            words = sys.argv[1:]
            
            for word in words:
                
                word = word.strip()
                
                if word != '':
                    
                    sys.stdout.write(word)
                    
                else:
                    
                    sys.stdout.write(' ')
                    
    else:
        
        sys.stdout.write('Usage: python remove-words.py [numbers]')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
