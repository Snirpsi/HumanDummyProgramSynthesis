#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), RemoveWordsHandler)
    print('Serving on port {}'.format(port))
    httpd.serve_forever()
    
