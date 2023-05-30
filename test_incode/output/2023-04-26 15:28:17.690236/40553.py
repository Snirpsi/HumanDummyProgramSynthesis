#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers or iterates over a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        # Parse the arguments
        
        port = int(sys.argv[1])
        
    else:
        
        # Print the list of numbers
        
        port = 5000
        
    
    # Create the server
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Start the server
    
    server.serve_forever()
    
    
