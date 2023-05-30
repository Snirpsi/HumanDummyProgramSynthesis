#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port and prints fruits. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitHandler)
    
    server.serve_forever()

<|/ file filename=fruit.py source=github |>