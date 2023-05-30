#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    
    print("Starting server on port " + str(port))
    
    server = Server()
    server.serve_forever()
    
