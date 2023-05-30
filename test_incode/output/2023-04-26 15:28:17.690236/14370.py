#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port. """    
    while True:
        port = int(input('Enter a port number: '))
        if port == -1:
            break
        print('The port number is:', port)
        print('The port name is:', get_port_name(port))
        print('The port description is:', get_port_description(port))
        print('The port type is:', get_port_type(port))
        print('The port state is:', get_port_state(port))
        print('The port status is:', get_port_status(port))
        print('The port 