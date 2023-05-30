#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a port or adds a list of words. """    
    port = ''
    words = []
    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        
        words = input('Enter a word: ').split()
        
        if len(words) == 0:
            continue
        
        if port in ports:
            ports[port] = words
        else:
            print('Port number {} is not in ports list.'.format(port))
    
    print('Ports:')
    for port in ports:
        print('\t{}'.format(port))
    
    print('\nWords:')
    for word in words:
        print('\t{}'.format(word))
    
    print('\nPorts:')
    for port in ports:
        print('\t{}'.format(port))
    
    print('\nWords:')
    for word in words:
        print('\t{}'.format(word))
    
    print('\nPorts:')
    for port in ports:
        print('\t{}'.format(port))
    
    print('\nWords:')
    for word in words:
        print('\t{}'.format(word))
    
    print('\nPorts:')
    for port in ports:
        print('\t{}'.format(port))
    
    print('\nWords:')
    for word in words:
        print('\t{}'.format(word))
    
    print('\nPorts:')
    for port in ports:
        print('\t{}'.format(port))
    
    print('\nWords:')
    for word in words:
        print('\t{}'.format(word))
    
    print('\nPorts:')
    for port in ports:
        print('\t{}'.format(port))
    
    print('\nWords:')
    for word in words:
        print('\t{}'.format(word))
    
    print('\nPorts:')
    for port in ports:
        print('\t{}'.format(port))
    
    print('\nWords:')
    for word in words:
        print('\t{}'.format(word))
    
    print('\nPorts:')
    for port in ports:
        print('\t{}'.format(port))
    
    print('\nWords:')
    for word in words:
        print('\t{}'.format(word))
    
    print('\nPorts:')
    for port in ports:
        print('\t{}'.format(port))
    
    print('\nWords:')
    for word in words:
        print('\t{}'.format(word))
    
    print('\nPorts:')
    for port in ports:
        print('\t{}'.format(port))
    
    print('\nWords:')
    for word in words:
        print('\t{}'.format(word))
    
    print('\nPorts:')
    for port in ports:
        print('\t{}'.format(port))
    
    print('\nWords:')
    for word in words:
        print('\t{}'.format(word))
    
    print('\nPorts:')
    for port in ports:
        print('\t{}'.format(port))
    
    print('\nWords:')
