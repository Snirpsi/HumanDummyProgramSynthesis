#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports or removes words. """    
    
    ports = range(8000, 9000)
    
    for port in ports:
        httpd = HTTPServer(('localhost', port), WordsHandler)
        httpd.serve_forever()
    
    print('Server stopped.')
    
