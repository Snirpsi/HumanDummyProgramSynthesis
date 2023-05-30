#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers and returns all ports. """    
    ports = []
    while True:
        ports.append(random.randint(1024, 65535))
        print("Port {} is open".format(ports[-1]))
        time.sleep(1)
        
