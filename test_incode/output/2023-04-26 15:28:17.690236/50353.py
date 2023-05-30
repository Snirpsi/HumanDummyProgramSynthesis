#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    
    ports = []
    
    # Get the ports used by the webserver
    ports.extend(get_ports())
    
    # Get the ports used by the client (to test the webserver)
    ports.extend(get_ports(client=True))
    
    # Get the ports used by the server (to test the client)
    ports.extend(get_ports(server=True))
    
    # Print the ports used by the webserver
    for port in ports:
        print(port)
    
    # Run the webserver
    run(ports, host='0.0.0.0')
    
    # Run the client (to test the webserver)
    run(ports, host='127.0.0.1')
    
    # Run the server (to test the client)
    run(ports, host='::1')
    
    # Run the server (to test the client)
    run(ports, host='::')
    
    # Run the server (to test the client)
    run(ports, host='127.0.0.1')
    
    # Run the server (to test the client)
    run(ports, host='127.0.0.1')
    
    # Run the server (to test the client)
    run(ports, host='127.0.0.1')
    
    # Run the server (to test the client)
    run(ports, host='127.0.0.1')
    
    # Run the server (to test the client)
    run(ports, host='127.0.0.1')
    
    # Run the server (to test the client)
    run(ports, host='127.0.0.1')
    
    # Run the server (to test the client)
    run(ports, host='127.0.0.1')
    
    # Run the server (to test the client)
    run(ports, host='127.0.0.1')
    
    # Run the server (to test the client)
    run(ports, host='127.0.0.1')
    
    # Run the server (to test the client)
    run(ports, host='127.0.0.1')
    
    # Run the server (to test the client)
    run(ports, host='127.0.0.1')
    
    # Run the server (to test the client)
    run(ports, host='127.0.0.1')
    
    # Run the server (to test the client)
    run(ports, host='127.0.0.1')
    
    # Run the server (to test the client)
    run(ports, host='127.0.0.1')
    
    # Run the server (to test the client)
    run(ports, host='127.0.0.1')
    
    # Run the server (to test the client)
    run(ports, host='127.0.0.1')
    
    # Run the server (to test the client)
    run(ports, host='127.0.0.1')
    
