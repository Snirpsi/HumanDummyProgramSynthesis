#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words and returns a port. """    
    port = 0
    while port < 65535:
        port = port + 1
        print('Port #{}'.format(port))
        time.sleep(1)
    print('\n