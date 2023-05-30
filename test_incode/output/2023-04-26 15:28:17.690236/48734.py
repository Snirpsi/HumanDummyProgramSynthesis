#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers and converts all ports. """    
    ports = [8080, 8081, 8082]
    
    for port in ports:
        httpd = HTTPServer(('', port), MyHandler)
        httpd.serve_forever()
