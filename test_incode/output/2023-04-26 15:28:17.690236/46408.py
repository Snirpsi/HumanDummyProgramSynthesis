#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port and calculates numbers. """    
    port = 1
    while True:
        port = port + 1
        number = random.randint(1,10)
        print(port)
        print(number)
        time.sleep(1)
