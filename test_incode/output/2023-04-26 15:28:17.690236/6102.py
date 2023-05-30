#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input. """    
    import sys
    
    # Parse command line arguments
    args = sys.argv[1:]
    
    # Start server
    server = HTTPServer(('', 8080), RequestHandler)
    
    # Start web server
    server.serve_forever()
    
