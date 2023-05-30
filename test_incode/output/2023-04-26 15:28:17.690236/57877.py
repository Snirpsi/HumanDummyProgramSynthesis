#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and opens a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), NumberServer)
    server.serve_forever()
    
