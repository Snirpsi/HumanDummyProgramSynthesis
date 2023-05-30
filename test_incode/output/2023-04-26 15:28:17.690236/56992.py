#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or opens a port. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), WordsHandler)
    httpd.serve_forever()
    
