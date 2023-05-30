#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers or opens numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), NumbersHandler)
    
    print("Serving at port", port)
    
    server.serve_forever()

<|/ file ext=.py |>