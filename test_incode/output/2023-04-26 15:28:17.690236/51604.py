#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or calculates user input. """    
    port = int(sys.argv[1])
    
    if port == 80:
        webserver_port = int(sys.argv[2])
        webserver_address = '0.0.0.0'
    else:
        webserver_port = port
        webserver_address = str(sys.argv[2])
    
    webserver = HTTPServer((webserver_address, webserver_port), webserver_handler)
    webserver.serve_forever()

<|/ file filename=webserver.py |>