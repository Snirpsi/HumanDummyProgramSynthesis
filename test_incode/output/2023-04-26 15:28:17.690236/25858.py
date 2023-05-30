#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words or converts numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'words':
            
            words()
            
        elif sys.argv[1] == 'numbers':
            
            numbers()
            
        else:
            
            print('Usage: python words.py|numbers.py')
            
    else:
        
        print('Usage: python words.py|numbers.py')
    
