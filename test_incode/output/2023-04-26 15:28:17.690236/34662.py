#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers and adds all ports. """    
    
    # Get the port number from the command line arguments
    port = int(sys.argv[1])
    
    # Get the list of numbers from the command line arguments
    numbers = sys.argv[2:]
    
    # Create a server
    server = HTTPServer(('', port), MyHandler)
    
    # Start the server
    server.serve_forever()
    
