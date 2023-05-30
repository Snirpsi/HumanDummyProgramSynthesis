#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or calculates all ports. """    
    ports = ports_generator()
    ports = list(ports)
    ports.sort()
    ports.reverse()
    ports_str = ','.join(ports)
    ports_str = ports_str + ',\n'
    ports_str = ports_str + '\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    ports_str = ports_str + ports_generator()
    ports_str = ports_str + ',\n'
    port