#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words and adds all ports. """    
    
    ports = []
    
    ports.append(8080)
    ports.append(8000)
    
    ports_str = ','.join(str(port) for port in ports)
    
    webserver.run(host='0.0.0.0', port=int(ports_str))
    
