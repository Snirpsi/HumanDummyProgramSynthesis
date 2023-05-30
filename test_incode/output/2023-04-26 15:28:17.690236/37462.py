#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words and adds all ports. """    
    ports = []
    words = open("words.txt").read().splitlines()
    
    for word in words:
        ports.append(word.split(":")[0])
    
    ports = list(set(ports))
    
    return ports
<|/ file source=github dstars=0 |>