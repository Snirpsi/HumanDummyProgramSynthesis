#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port and calculates words. """    
    port = int(sys.argv[1])
    words = calc_words(port)
    print(words)

<|/ file filename=wordcount.py |>