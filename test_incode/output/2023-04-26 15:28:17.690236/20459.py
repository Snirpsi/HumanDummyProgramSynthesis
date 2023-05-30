#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    server = HTTPServer(("", 8080), FruitHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()

<|/ file ext=.py |>