#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port or prints numbers. """    
    while True:
        port = random.randint(10000, 20000)
        print(port)
        time.sleep(1)
