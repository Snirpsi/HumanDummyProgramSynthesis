#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports or prints a list of words. """    
    while True:
        ports = find_ports()
        words = []
        for port in ports:
            words.append(port[0])
        print(" ".join(words))
        time.sleep(1)
        
