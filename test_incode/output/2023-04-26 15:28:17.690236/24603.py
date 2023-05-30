#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words or stores fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'words':
            
            words = ['apple', 'banana', 'orange', 'mango', 'kiwi', 'grape', 'plum']
            
            print('\n'.join(words))
            
        elif sys.argv[1] == 'fruits':
            
            fruits = ['apple', 'banana', 'orange', 'mango', 'kiwi', 'grape', 'plum']
            
            print('\n'.join(fruits))
            
        else:
            
            print('Usage: %s [words|fruits]' % sys.argv[0])
            
    else:
        
        print('Usage: %s [words|fruits]' % sys.argv[0])
        
