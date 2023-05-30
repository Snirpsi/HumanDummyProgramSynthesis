#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers and multiplyes all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    ports = [p * 2 for p in ports]
    ports = list(set(ports))
    ports.sort()
    
    httpd = HTTPServer(("", ports[0]), Handler)
    httpd.serve_forever()
    
