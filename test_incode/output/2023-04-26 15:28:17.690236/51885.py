#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or calculates a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(0)
    
    words = sys.argv[1:]
    
    port = 0
    
    for word in words:
        port += word_to_port(word)
    
    print(port)
    
