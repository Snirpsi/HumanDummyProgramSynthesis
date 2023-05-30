#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers. """    
    
    # Parse the command line arguments
    port = int(sys.argv[1])
    
    # Create the server
    server = HTTPServer(('', port), MyHandler)
    
    # Run the server
    server.serve_forever()
    
