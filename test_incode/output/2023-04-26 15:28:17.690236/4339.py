#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports or enumerates numbers. """    
    ports = []
    
    ports.append(80)
    ports.append(443)
    
    ports.reverse()
    
    for port in ports:
        print("Starting port {} ...".format(port))
        
        httpd = HTTPServer(('', port), Handler)
        httpd.serve_forever()
        
        print("Port {} stopped.".format(port))
