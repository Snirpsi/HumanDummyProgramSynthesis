#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports. """    
    while True:
        
        # Remove all ports
        subprocess.call(['iptables-save'])
        
        # Sleep for a second
        time.sleep(1)
        
