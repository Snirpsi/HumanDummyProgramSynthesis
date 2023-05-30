#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words or returns a list of words. """    
    
    # Parse command line arguments
    args = parse_args()
    
    # Create a server
    server = WebServer()
    
    # Start server
    server.serve()
    
    # Stop server
    server.stop()

<|/ file ext=.py source=github filename=webserver.py |>