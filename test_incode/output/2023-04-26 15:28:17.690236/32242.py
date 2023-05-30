#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers. """    
    
    httpd = HTTPServer(('', 8080), MyHandler)
    print('Serving at http://127.0.0.1:8080')
    httpd.serve_forever()
    
