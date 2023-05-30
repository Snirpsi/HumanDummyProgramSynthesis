#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words or returns all ports. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    ports = []
    
    for word in words:
        
        if word in ports:
            ports.remove(word)
        else:
            ports.append(word)
    
    for port in ports:
        print("Port %s: %s" % (port, words[port]))
    
