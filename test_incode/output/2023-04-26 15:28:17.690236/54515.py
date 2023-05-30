#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or calculates numbers. """    
    
    ports = []
    
    ports.append(8080)
    ports.append(8000)
    
    ports.reverse()
    
    for port in ports:
        
        print("Starting webserver on port " + str(port))
        
        httpd = HTTPServer(('', port), Handler)
        httpd.serve_forever()
        
