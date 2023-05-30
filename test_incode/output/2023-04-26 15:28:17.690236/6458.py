#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input and calculates all ports. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A program that converts user input and calculates all ports.')
    parser.add_argument('port', metavar='PORT', type=int, nargs='?', help='The port to convert')
    args = parser.parse_args()
    
    # Convert user input to an integer
    port = int(args.port)
    
    # Calculate all ports
    ports = calculate_all_ports(port)
    
    # Print all ports
    for port in ports:
        print(port)
