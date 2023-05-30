#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports and multiplyes user input. """    
    ports = [int(i) for i in sys.argv[1:]]
    
    server_address = ("", ports[0])
    
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()
    
