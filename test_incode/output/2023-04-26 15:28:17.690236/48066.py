#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or adds a port. """    
    port = int(sys.argv[1])
    
    # Create a server
    httpd = HTTPServer(("", port), MyHandler)
    
    # Run the server
    httpd.serve_forever()
