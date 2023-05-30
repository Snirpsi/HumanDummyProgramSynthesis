#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits or adds a port. """    
    port = int(sys.argv[1])
    
    # Create a server
    httpd = HTTPServer(('localhost', port), FruitServer)
    
    # Start the server
    httpd.serve_forever()
    
