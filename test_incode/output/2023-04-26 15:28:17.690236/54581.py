#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words or stores all ports. """    
    
    ports = range(65535)
    
    httpd = HTTPServer(('', 0), WordsServer)
    httpd.serve_forever()
