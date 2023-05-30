#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports and iterates over a list of numbers. """    
    ports = []
    for port in range(1, 65535):
        ports.append(port)
    
    httpd = HTTPServer(("", ports[0]), SimpleHTTPRequestHandler)
    print("Serving at port " + str(ports[0]))
    httpd.serve_forever()
    
