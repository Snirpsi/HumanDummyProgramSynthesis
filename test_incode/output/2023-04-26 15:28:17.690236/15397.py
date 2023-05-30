#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a port or calculates fruits. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A program that stores a port or calculates fruits.')
    parser.add_argument('port', help='The port to store or calculate')
    args = parser.parse_args()
    
    # Store the port
    if args.port is not None:
        port = args.port
    else:
        port = input('Enter the port to store or calculate: ')
    
    # Calculate the fruit
    fruit(port)
    
