#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits. """    
    
    # Define the server's address and port
    server_address = ("", 8000)
    
    # Create the server
    server = HTTPServer(server_address, FruitHandler)
    
    # Start the server
    server.serve_forever()

<|/ file source=github filename=fruits.py |>