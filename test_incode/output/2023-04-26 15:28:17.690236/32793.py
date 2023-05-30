#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or stores all ports. """    
    
    # Start the webserver
    httpd = HTTPServer(('', 8000), WordsServer)
    httpd.serve_forever()
    
