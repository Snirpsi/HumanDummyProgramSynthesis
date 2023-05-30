#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and stores all ports. """    
    port = 8080
    
    server = HTTPServer(('', port), MyHandler)
    server.serve_forever()
