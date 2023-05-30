#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or calculates a list of numbers. """    
    ports = range(1,65535)
    ports_str = [str(p) for p in ports]
    ports_str = ",".join(ports_str)
    print(ports_str)
