#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words or multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'words':
            
            words = []
            
            for word in sys.argv[2:]:
                
                words.append(word.lower())
            
            print(words)
            
        elif sys.argv[1] == 'multiply':
            
            numbers = []
            
            for number in sys.argv[2:]:
                
                numbers.append(int(number))
            
            print(numbers)
            
    else:
        
        print('Usage: %s [words|multiply]' % sys.argv[0])
        
