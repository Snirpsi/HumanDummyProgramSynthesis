#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and multiplyes all ports. """    
    port = int(sys.argv[1])
    ports = [port for i in range(10)]
    ports_str = [str(port) for port in ports]
    ports_str = ','.join(ports_str)
    
    