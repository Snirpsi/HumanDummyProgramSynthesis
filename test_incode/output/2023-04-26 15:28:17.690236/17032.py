#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers or enumerates a list of words. """    
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, Calculator)
    httpd.serve_forever()

<|/ file source=github filename=calculator.py |>