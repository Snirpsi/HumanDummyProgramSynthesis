#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or converts user input. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    print('Starting httpserver on port %s' % port)
    httpd.serve_forever()

