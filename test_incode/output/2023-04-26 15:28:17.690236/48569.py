#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers or prints all ports. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    httpd = HTTPServer(("", ports[0]), SimpleHTTPRequestHandler)
    print("Serving on port {}".format(ports[0]))
    httpd.serve_forever()
    
