#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or stores a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    numbers = []
    
    with open(filename) as fp:
        for line in fp:
            numbers.append(int(line))
    
    print("\n".join(map(str, numbers)))

<|/ file source=github filename=