#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    ports = range(8000, 9000)
    
    for port in ports:
        httpd = make_server(port, "", Handler)
        print("Serving on port {}".format(port))
        httpd.serve_forever()
        
