#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports or stores a list of words. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    words = []
    
    for port in ports:
        words.append(str(port) + ":