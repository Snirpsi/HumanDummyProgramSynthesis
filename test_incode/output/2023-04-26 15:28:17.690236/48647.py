#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), RequestHandler)
    httpd.serve_forever()
    
