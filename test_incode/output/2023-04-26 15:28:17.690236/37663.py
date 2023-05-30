#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words and removes numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    print('Starting server')
    httpd.serve_forever()
