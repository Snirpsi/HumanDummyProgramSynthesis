#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port and enumerates a list of words. """    
    port = int(sys.argv[1])
    words = []
    
    for i in range(port):
        words.append(i)
    
    print(words)

<|/ file source=github |>