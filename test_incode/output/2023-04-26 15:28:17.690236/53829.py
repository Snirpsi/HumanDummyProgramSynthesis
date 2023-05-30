#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or converts all ports. """    
    import sys
    ports = sys.argv[1:]
    
    words = []
    
    for port in ports:
        if port == '-':
            port = 'all'
        
        if port == 'all':
            words.append('all')
        else:
            words.append(port)
    
    for word in words:
        print(word)
        
    if len(words) == 0:
        print('No ports found')
    else:
        print('All ports found')
        
    
