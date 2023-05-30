#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    ports = [int(i) for i in sys.argv[1:]]
    
    httpd = HTTPServer(('', ports[0]), MultiplyingServer)
    httpd.serve_forever()
    
