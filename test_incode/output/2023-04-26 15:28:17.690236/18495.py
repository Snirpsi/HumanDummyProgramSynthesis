#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports or calculates a list of words. """    
    ports = openPorts()
    words = []
    for port in ports:
        words.append(port.readLine().strip())
    print(words)
    
