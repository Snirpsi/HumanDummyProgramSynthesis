#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words and prints a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    print('Serving on port {}'.format(port))
    httpd.serve_forever()

<|/ file filename=words-server.py |>