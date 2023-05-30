#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    import sys
    
    webserver_port = int(sys.argv[1])
    
    httpd = HTTPServer(('', webserver_port), MyHandler)
    
    print('Serving at http://127.0.0.1:{}'.format(webserver_port))
    httpd.serve_forever()
    
