#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or converts a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [port] or [word]" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    if len(sys.argv) >= 3:
        words = sys.argv[2:]
    else:
        words = []
    
    ports = enumeratePorts(port)
    
    for port, word in ports:
        if word in words:
            print(port)
        else:
            print("%s is not in %s" % (word, words))
    
    sys.exit()
    
if __name__ == "__main__":
    main()

<|/ file source=github ext=.py |>