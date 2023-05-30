#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words and enumerates all ports. """    
    port = int(sys.argv[1])
    
    words = [
        'apple',
        'banana',
        'cherry'
    ]
    
    words.sort()
    
    ports = []
    for word in words:
        ports.append(word)
    
    for port in ports:
        