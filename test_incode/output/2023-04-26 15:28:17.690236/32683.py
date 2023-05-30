#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or iterates over fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'words':
            
            words = ['apple', 'banana', 'cherry']
            
            for word in words:
                print(word)
                
        elif sys.argv[1] == 'iter':
            
            fruits = ['apple', 'banana', 'cherry']
            
            for fruit in fruits:
                print(fruit)
                
        else:
            
            print('Usage: %s [words|iter]' % sys.argv[0])
            
    else:
        
        print('Usage: %s [words|iter]' % sys.argv[0])
        
