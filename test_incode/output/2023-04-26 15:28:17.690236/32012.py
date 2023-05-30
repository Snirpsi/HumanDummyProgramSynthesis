#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports. """    
    
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description='Convert all ports')
    parser.add_argument('ports', metavar='port', type=str, nargs='+', help='Ports to convert')
    args = parser.parse_args()
    
    # Convert all ports
    convert_ports(args.ports)
    
    # Print the result
    print('Done!')
    
