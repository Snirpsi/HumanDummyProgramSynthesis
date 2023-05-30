#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers and removes a list of words. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    print('Serving at port ' + str(port) + '...')
    httpd.serve_forever()
    
