#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and prints numbers. """    
    port = int(sys.argv[1]) # get port from command line
    
    # start webserver
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # start a thread to serve requests
    httpd.serve_forever()
    
