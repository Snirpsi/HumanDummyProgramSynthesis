#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers. """    
    port = int(sys.argv[1])
    
    # Create a server
    httpd = HTTPServer(('', port), MyHandler)
    
    # Start it
    httpd.serve_forever()
