#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port and enumerates words. """    
    port = int(sys.argv[1])
    words = []
    for word in range(port):
        words.append(str(word))
    print(" ".join(words))

<|/ file filename=port