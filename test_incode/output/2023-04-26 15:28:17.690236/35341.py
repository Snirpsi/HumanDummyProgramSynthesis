#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or converts a port. """    
    import sys
    import argparse
    parser = argparse.ArgumentParser(description='Enumerate or convert a port')
    parser.add_argument('port', nargs='?', help='port to enumerate')
    args = parser.parse_args()
    if args.port is None:
        parser.print_help()
        sys.exit(0)
    port = args.port
    
    port_list = list()
    
    try:
        port_list = list(get_ports(port))
    except Exception as ex:
        print(ex)
        sys.exit(0)
    
    for port in port_list:
        print(port)
        
    if len(port_list) == 0:
        print('No ports found')
        sys.exit(0)
    
    if len(port_list) == 1:
        port_list = port_list[0]
    
    port_list_str = ','.join(port_list)
    
    print('Ports found: ' + port_list_str)
    
