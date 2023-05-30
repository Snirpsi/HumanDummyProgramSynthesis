#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port and multiplyes numbers. """    
    while True:
        port = random.randint(1, 65535)
        number = random.randint(1, 65535)
        print(port, number)
        time.sleep(1)
