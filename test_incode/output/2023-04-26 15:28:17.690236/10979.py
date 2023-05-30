#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers or removes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'list':
            
            list_numbers(sys.argv[2])
            
        elif sys.argv[1] == 'remove':
            
            remove_word(sys.argv[2])
            
        else:
            
            print('Usage: %s [list|remove]' % sys.argv[0])
            
    else:
        
        print('Usage: %s [list|remove]' % sys.argv[0])
    
