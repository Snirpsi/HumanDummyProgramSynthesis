#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports and enumerates a list of words. """    
    ports = enumeratePorts()
    words = []
    for port, word in ports:
        words.append(word)
    print(words)
    
<|/ file source=github dstars=0 |>