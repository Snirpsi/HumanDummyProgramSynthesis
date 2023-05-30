#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits. """    
    
    httpd = HTTPServer(('', 8000), MyHandler)
    print('Serving at port 8000...')
    httpd.serve_forever()
    
