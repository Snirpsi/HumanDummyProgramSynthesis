#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and opens all ports. """    
    ports = list( range( 0, 65535 ) )
    
    httpd = HTTPServer( ('', 80), MyHandler )
    httpd.serve_forever()
    
