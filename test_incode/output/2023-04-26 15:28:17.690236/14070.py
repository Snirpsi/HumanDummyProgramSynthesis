#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits or stores a list of words. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, FruitHandler)
    httpd.serve_forever()

<|/ file filename=webserver.py source=github |>