#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports or opens all ports. """    
    ports = range(8000, 8100)
    
    httpd = HTTPServer(("", 8000), MyHandler)
    httpd.serve_forever()
