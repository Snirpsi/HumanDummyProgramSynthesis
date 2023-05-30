#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port or prints a list of words. """    
    
    port = int(sys.argv[1])
    
    if port == -1:
        print('Usage: python listwords.py port')
    else:
        words = []
        
        for i in range(port):
            words.append(str(i))
        
        print('\n'.join(words))
        
