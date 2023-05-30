#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or prints a list of numbers. """    
    ports = []
    
    ports.append(8080)
    ports.append(8088)
    ports.append(8181)
    
    for port in ports:
        print("Starting port {}".format(port))
        
        httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
        httpd.serve_forever()
        
