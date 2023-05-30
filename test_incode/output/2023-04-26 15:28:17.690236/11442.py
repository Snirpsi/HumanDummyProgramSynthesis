#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    ports = range(8080, 8081)
    
    for port in ports:
        server = HTTPServer(("", port), SimpleHTTPRequestHandler)
        print("serving at port ", port)
        server.serve_forever()
        
