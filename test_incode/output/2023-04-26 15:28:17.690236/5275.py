#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits or removes a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['apple', 'banana', 'orange', 'kiwi']
    
    server = HTTPServer(('', 8080), FruitServer)
    
    server.serve_forever()
    
