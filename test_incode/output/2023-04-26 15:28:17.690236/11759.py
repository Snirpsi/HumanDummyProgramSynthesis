#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port and returns words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        words = []
        
        for i in range(port):
            words.append(str(i))
            
        words.append(str(port))
        
        print('\n'.join(words))
    else:
        print('Usage: python word