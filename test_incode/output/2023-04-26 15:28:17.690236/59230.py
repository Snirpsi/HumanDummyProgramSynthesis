#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers or stores fruits. """    
    
    # Setup a webserver
    server = HTTPServer(('', 8000), RequestHandler)
    
    # Start the webserver
    server.serve_forever()

<|/ file source=github filename=server.py |>