#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports or iterates over user input. """    
    
    ports = range(8000, 8100)
    
    for port in ports:
        httpd = HTTPServer(('', port), MyHandler)
        httpd.serve_forever()
        
