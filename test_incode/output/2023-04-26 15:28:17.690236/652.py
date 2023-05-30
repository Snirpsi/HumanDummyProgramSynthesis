#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers and stores a list of numbers. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), RequestHandler)
    httpd.serve_forever()

<|/ file filename=server.py |>