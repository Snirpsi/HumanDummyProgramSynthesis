#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words or converts all ports. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = []
    for word in sys.argv[1:]:
        words.append(word)
    
    ports = ports_converter(words)
    
    for port in ports:
        port