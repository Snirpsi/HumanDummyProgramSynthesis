#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words. """    
    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    server = HTTPServer(("", 80), WordsServer)
    server.serve_forever()
    
