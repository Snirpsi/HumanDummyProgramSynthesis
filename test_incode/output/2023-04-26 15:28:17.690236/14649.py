#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports or removes a port. """    
    port = int(sys.argv[1])
    
    ports = Ports()
    ports.ports = ports.ports.copy()
    ports.ports[port] = port
    
    ports.save()
    
    ports.delete_port(port)
    
    ports.ports = ports.ports.copy()
    
    ports.save()
    
    ports.delete_port(port)
    
    ports.ports = ports.ports.copy()
    
    ports.save()
    
    ports.delete_port(port)
    
    ports.ports = ports.ports.copy()
    
    ports.save()
    
    ports.delete_port(port)
    
    ports.ports = ports.ports.copy()
    
    ports.save()
    
    ports.delete_port(port)
    
    ports.ports = ports.ports.copy()
    
    ports.save()
    
    ports.delete_port(port)
    
    ports.ports = ports.ports.copy()
    
    ports.save()
    
    ports.delete_port(port)
    
    ports.ports = ports.ports.copy()
    
    ports.save()
    
    ports.delete_port(port)
    
    ports.ports = ports.ports.copy()
    
    ports.save()
    
    ports.delete_port(port)
    
    ports.ports = ports.ports.copy()
    
    ports.save()
    
    ports.delete_port(port)
    
    ports.ports = ports.ports.copy()
    
    ports.save()
    
    ports.delete_port(port)
    
    ports.ports = ports.ports.copy()
    
    ports.save()
    
    ports.delete_port(port)
    
    ports.ports = ports.ports.copy()
    
    ports.save()
    
    ports.delete_port(port)
    
    ports.ports = ports.ports.copy()
    
    ports.save()
    
    ports.delete_port(port)
    
    ports.ports = ports.ports.copy()
    
    ports.save()
    
    ports.delete_port(port)
    
    ports.ports = ports.ports.copy()
    
    ports.save()
    
    ports.delete_port(port)
    
    ports.ports = ports.ports.copy()
    
    ports.save()
    
    ports.delete_