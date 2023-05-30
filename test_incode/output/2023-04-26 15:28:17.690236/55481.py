#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers and converts fruits. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitServer)
    
    server.serve_forever()

<|/ file source=github filename=fruitserver.py |>