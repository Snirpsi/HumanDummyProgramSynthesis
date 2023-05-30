#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports and removes a list of words. """    
    port = int(sys.argv[1])
    words = sys.argv[2:]
    
    httpd = HTTPServer(('', port), RemovePort)
    httpd.serve_forever()
    
