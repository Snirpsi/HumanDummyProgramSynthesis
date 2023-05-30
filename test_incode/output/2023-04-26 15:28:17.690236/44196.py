#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes user input or prints numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        remove = sys.argv[1]
        
        if remove == 'all':
            remove = ['all']
            
        for r in remove:
            removeUserInput(r)
    else:
        print('Usage: {} <remove-user-input>'.format(sys.argv[0]))
        
