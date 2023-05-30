#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port or prints a list of numbers. """    
    while True:
        port = random.randint(1, 65535)
        print("Port number is", port)
        time.sleep(1)
        
