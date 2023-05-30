#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or prints user input. """    
    port = int(sys.argv[1])
    
    # Create a server
    httpd = HTTPServer(("", port), MyHandler)
    
    # Start it
    httpd.serve_forever()
    
