#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or removes a port. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(1)
    
    words = sys.argv[1:]
    
    words = [word.lower() for word in words]
    
    words = remove_ports(words)
    
    print("\n".join(words))

<|/ file filename=remove-ports.py ext=.py |>