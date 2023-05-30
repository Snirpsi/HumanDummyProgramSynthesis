#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port or returns a list of words. """    
    port = '/dev/ttyUSB0'
    words = []
    for line in open('/dev/ttyUSB0'):
        line = line.strip()
        if line == '':
            words.append('')
        else:
            words.append(line)
    return words

<|/ file filename=ttyUSB.py source=github |>