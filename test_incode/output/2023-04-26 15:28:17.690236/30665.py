#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words or adds all ports. """    
    
    words = []
    
    for word in sys.argv[1:]:
        words.append(word)
    
    ports = sys.argv[2:]
    
    for port in ports:
        port = int(port)
        
        if port < 1 or port > 65535:
            print('Port must be between 1 and 65535.')
            sys.exit(1)
        
        if port not in ports:
            print('Port must be one of: ' + str(ports))
            sys.exit(1)
        
        words.append(port)
    
    words.sort()
    
    for word in words:
        print('