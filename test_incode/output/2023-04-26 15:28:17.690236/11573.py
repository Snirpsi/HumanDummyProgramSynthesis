#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and stores user input. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('Serving at port %s' % port)
    httpd.serve_forever()
    
