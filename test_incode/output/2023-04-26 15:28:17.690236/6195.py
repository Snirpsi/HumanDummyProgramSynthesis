#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port. """    
    
    # Get the port number
    port = int(sys.argv[1])
    
    # Remove port
    subprocess.call(['iptables', '-F', port])
    
    # Print the result
    print('Removed port {}.'.format(port))
