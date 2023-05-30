#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and calculates a list of words. """    
    port = int(sys.argv[1])
    words = []
    for i in range(0, port):
        words.append(str(i))
    print(" ".join(words))
    
    
<|/ file ext=.py source=github |>