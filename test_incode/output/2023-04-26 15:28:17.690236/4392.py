#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words or opens all ports. """    
    
    words = ['word1', 'word2', 'word3']
    
    while True:
        
        port = input('Enter a port number: ')
        
        if port == '':
            break
        
        print('Opening port %s' % port)
        
        