#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports or iterates over numbers. """    
    ports = range(1,65535)
    
    for port in ports:
        httpd = HTTPServer(('localhost', port), MyHandler)
        httpd.serve_forever()
