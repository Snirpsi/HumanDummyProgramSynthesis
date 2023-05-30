#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port. """    
    
    # Get the port number
    port = int(input("Enter the port number: "))
    
    # Remove the port
    subprocess.call(['iptables', '-D', 'INPUT', '-p', str(port), '-s', '