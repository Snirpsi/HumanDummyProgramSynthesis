#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port and stores words. """    
    port = 1
    words = []
    while True:
        port = port + 1
        words.append(str(port))
        print("Port " + str(port) + ": " + " ".join(words))
        time.sleep(1)
    
