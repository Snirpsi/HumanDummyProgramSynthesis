#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port and removes a list of words. """    
    port = '/dev/ttyUSB0'
    lines = open(port).readlines()
    for line in lines:
        line = line.strip()
        words = line.split()
        for word in words:
            if word not in ['#', '!']:
                print(word)
                