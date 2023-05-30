#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Remove all ports.')
    parser.add_argument('-p', '--ports', dest='ports', help='The ports to remove.', nargs='+')
    args = parser.parse_args()
    
    # Remove all ports
    remove_all_ports(args.ports)
    
