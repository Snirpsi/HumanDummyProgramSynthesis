#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port or opens a list of words. """    
    
    words = []
    
    while True:
        
        port = input('Enter a port number: ')
        
        if port == '':
            break
        
        try:
            port = int(port)
            
            if port < 0 or port > 65535:
                print('Invalid port number')
                continue
            
            words.append(port)
            
        except:
            print('Invalid port number')
            continue
    
    print('\n'.join(words))
    
