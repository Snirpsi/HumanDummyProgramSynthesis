#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or opens a list of numbers. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Start the webserver
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
