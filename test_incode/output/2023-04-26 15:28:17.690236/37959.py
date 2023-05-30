#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port. """    
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int, help='The port to enumerate.')
    args = parser.parse_args()
    
    port = args.port
    
    port_list = list(range(port))
    
    for port_number in port_list:
        print('Port number:', port_number)
    
    sys.exit(0)
