#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port. """    
    
    # Get the port number
    port = sys.argv[1]
    
    # Remove it
    subprocess.call(['iptables', '-D', 'INPUT', '-p', port, '-t', 'filter', '-j', 'DROP'])
    
    # Print the result
    print('Port {} has been removed'.format(port))
    
