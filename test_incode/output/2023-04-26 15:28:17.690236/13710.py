#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers and adds a list of words. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()

<|/ file ext=.py filename=server.py |>