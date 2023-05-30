#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and stores numbers. """    
    
    ports = []
    
    # Open the port and store its number in ports list.
    port = open('/tmp/ports.log', 'a')
    port.write('Port ' + str(os.getpid()) + '\n')
    port.close()
    
    # Start the webserver.
    httpd = make_server('', 8080, MyHandler)
    httpd.serve_forever()
    
    # Close the port and store its number in ports list.
    port.close()
    
    # Print the ports list.
    print('Ports list: ' + str(ports))
    
    
