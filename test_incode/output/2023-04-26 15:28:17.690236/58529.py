#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port. """    
    
    port = int(sys.argv[1]) # Port number
    
    server = HTTPServer(('', port), MyHandler)
    
    server.serve_forever()
    
