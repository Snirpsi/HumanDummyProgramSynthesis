#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words and prints all ports. """    
    ports = range(1,65535)
    while True:
        words = []
        for port in ports:
            words.append('port'+str(port))
        print('\n'.join(words))
        time.sleep(1)
