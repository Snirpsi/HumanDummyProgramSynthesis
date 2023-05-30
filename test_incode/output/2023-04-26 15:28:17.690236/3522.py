#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits or opens a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitServer)
    httpd.serve_forever()

<|/ file source=github filename=fruitserver.py |>