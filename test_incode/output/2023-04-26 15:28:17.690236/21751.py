#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input or multiplyes a port. """    
    
    port = int(sys.argv[1])
    
    if sys.argv[2] == 'add':
        port = port + int(sys.argv[3])
    elif sys.argv[2] == 'multiply':
        port = port * int(sys.argv[3])
    
    print("Serving on port {}".format(port))
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()

<|/ file filename=webserver.py |>