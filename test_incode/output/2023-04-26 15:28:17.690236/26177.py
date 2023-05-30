#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and opens numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    print('Serving at port %s' % port)
    httpd.serve_forever()
    
