#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or removes user input. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), WordsHandler)
    print('Starting httpd on port %s' % port)
    httpd.serve_forever()
    
