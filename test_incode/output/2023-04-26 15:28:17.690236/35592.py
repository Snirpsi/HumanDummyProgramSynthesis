#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or enumerates all ports. """    
    
    ports = range(5000, 5999)
    
    httpd = HTTPServer(("", ports[0]), WordsHandler)
    httpd.serve_forever()
    
