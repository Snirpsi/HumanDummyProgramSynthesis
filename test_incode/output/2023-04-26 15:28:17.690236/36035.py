#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words and multiplyes all ports. """    
    import sys
    
    wordlist = sys.argv[1:]
    
    for word in wordlist:
        ports = word.split(',')
        
        for port in ports:
            port = int(port)
            
            ports[port] = ports[port] * 2
            
        print(','.join(ports))
    
