#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words or prints numbers. """    
    
    # Start webserver
    webserver_address = ('localhost', 8080)
    webserver = HTTPServer(webserver_address, RequestHandler)
    webserver.serve_forever()

<|/ file source=github filename=webserver.py |>