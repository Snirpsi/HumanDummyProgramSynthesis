#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port and iterates over a list of words. """    
    import sys
    import time
    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    start = time.time()
    
    while True:
        port = input('Enter a port number: ')
        
        if port == 'exit':
            sys.exit()
        
        if port == '':
            print('Please enter a port number')
            continue
        
        port = int(port)
        
        if port < 0 or port > 65535:
            print('Please enter a port number between 0 and 65535')
            continue
        
        word = ''
        
        for word in words:
            if port == word:
                print('The word "{}" was found at port {}'.format(word, port))
                
                start = time.time()
                
                break
        
        end = time.time()
        
        print('The word "{}" was found at port {} took {} seconds'.format(word, port, end - start))
        
        time.sleep(1)
        
