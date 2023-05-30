#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports or multiplyes a list of numbers. """    
    
    ports = [8080, 8081, 8082]
    
    for port in ports:
        
        web = WebServer(port)
        web.serve_forever()
        
