#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input or adds words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        words = []
        
        for arg in sys.argv[1:]:
            
            if arg.startswith('-'):
                
                arg = '-' + arg[1:]
                
            words.append(arg)
            
        words = ' '.join(words)
        
        print('\n'.join(words))
        
    else:
        
        print('Usage: %s [-h] [-s STRING] [-d STRING] [-l STRING] [-n STRING] [-o STRING] [-c STRING] [-i STRING] [-w STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] [-y STRING] [-z STRING] [-r STRING] [-x STRING] 