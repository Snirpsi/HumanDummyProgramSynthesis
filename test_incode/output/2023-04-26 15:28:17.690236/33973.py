#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port and prints words. """    
    port = int(sys.argv[1])
    words = []
    for i in range(port):
        words.append(str(i))
    print(" ".join(words))

<|/ file source=github |>