#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a port. """    
    port = int(sys.argv[1])
    
    # Store the port in the database
    ports = Ports(port)
    ports.save()
    
    # Print the port in the terminal
    print(port)
    
    # Print the list of ports
    print(ports.ports)
    
    # Print the list of ports sorted by port
    print(ports.ports.order_by('port'))
    
    # Print the list of ports sorted by port and name
    print(ports.ports.order_by('port', 'name'))
    
    # Print the list of ports sorted by port and name
    print(ports.ports.order_by('port', 'name').all())
    
    # Print the list of ports sorted by port and name
    print(ports.ports.order_by('port', 'name').filter(name='test'))
    
    # Print the list of ports sorted by port and name
    print(ports.ports.order_by('port', 'name').filter(name='test').all())
    
    # Print the list of ports sorted by port and name
    print(ports.ports.order_by('port', 'name').filter(name='test').filter(name='test2'))
    
    # Print the list of ports sorted by port and name
    print(ports.ports.order_by('port', 'name').filter(name='test').filter(name='test2').all())
    
    # Print the list of ports sorted by port and name
    print(ports.ports.order_by('port', 'name').filter(name='test').filter(name='test2').filter(name='test3'))
    
    # Print the list of ports sorted by port and name
    print(ports.ports.order_by('port', 'name').filter(name='test').filter(name='test2').filter(name='test3').filter(name='test4'))
    
    # Print the list of ports sorted by port and name
    print(ports.ports.order_by('port', 'name').filter(name='test').filter(name='test2').filter(name='test3').filter(name='test4').filter(name='test5'))
    
    # Print the list of ports sorted by port and name
    print(ports.ports.order_by('port', 'name').filter(name='test').filter(name='test2').filter(name='test3').filter(name='test4').filter(name='test5').filter(name='test6'))
    
    # Print the list of ports sorted by port and name
    print(ports.ports.order_by('port', 'name').filter(name='test').filter(name='test2').filter(name='test3').filter(name='test4').filter(name='test5').filter(name='test6').filter(name='test