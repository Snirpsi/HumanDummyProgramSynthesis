#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    port = 8080
    
    # Create the server
    server = HTTPServer(('', port), MyHandler)
    
    # Start the server
    server.serve_forever()

<|/ file source=github filename=server.py |>