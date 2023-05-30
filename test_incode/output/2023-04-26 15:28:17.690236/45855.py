#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and enumerates words. """    
    port = 1
    words = []
    while True:
        port = port + 1
        words.append(str(port))
        print('Port ' + str(port) + ' is now ' + ', '.join(words))
        time.sleep(1)
        
