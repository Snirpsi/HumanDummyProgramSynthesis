#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or adds user input. """    
    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 1
    
    httpd = HTTPServer(("", port), MyHandler)
    
    print("Serving at port", port)
    
    httpd.serve_forever()

<|/ file filename=server.py source=github |>