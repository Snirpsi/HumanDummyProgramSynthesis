#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or opens all ports. """    
    
    # Start server
    server = HTTPServer(('0.0.0.0', 8080), WordsServer)
    server.serve_forever()
    
