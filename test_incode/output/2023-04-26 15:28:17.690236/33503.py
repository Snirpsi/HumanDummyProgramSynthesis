#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports and stores words. """    
    ports = open('/etc/service/words', 'r')
    words = ports.readlines()
    ports.close()
    
    for word in words:
        print(word)
        
