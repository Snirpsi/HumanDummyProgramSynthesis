#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts fruits or enumerates all ports. """    
    ports = enumerate_ports()
    for port in ports:
        port_name = port[0]
        port_type = port[1]
        port_id = port[2]
        port_name = port_name.capitalize()
        port_type = port_type.capitalize()
        print("Port: " + port_name + " Type: " + port_type + " ID: " + port_id)
    
