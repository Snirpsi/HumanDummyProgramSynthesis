#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or multiplyes a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    print('Serving on port ' + str(port) + '...')
    httpd.serve_forever()
