#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port and iterates over a list of words. """    
    port = 1
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    while True:
        port = port + 1
        print('Port ' + str(port) + ' is listening on ' + ', '.join(words))
        time.sleep(1)
