#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports or multiplyes all ports. """    
    ports = [int(port) for port in sys.argv[1:]]
    ports = [port * 2 for port in ports]
    ports = list(set(ports))
    ports.sort()
    ports = list(map(str, ports))
    ports = ','.join(ports)
    
    httpd = HTTPServer(("", ports[0]), Handler)
    httpd.serve_forever()
    
