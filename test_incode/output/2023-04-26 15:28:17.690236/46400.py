#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or removes a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()

<|/ file source=github |>