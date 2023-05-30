#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers and opens a list of words. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    print('Serving at port', port)
    httpd.serve_forever()

<|/ file source=github |>