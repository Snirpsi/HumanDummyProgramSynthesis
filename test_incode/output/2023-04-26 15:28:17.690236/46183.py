#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port and returns numbers. """    
    
    ports_to_remove = []
    
    # Read in ports list
    with open('ports.txt', 'r') as ports_file:
        ports_to_remove = ports_file.read().splitlines()
    
    # Remove ports
    for port in ports_to_remove:
        os.system('sudo iptables -t nat -D PREROUTING -p tcp --dport %s -j DNAT --to-destination %s:%s' % (port, sys.argv[1], sys.argv[2]))
    
    # Print number of ports removed
    print('Number of ports removed: %d' % len(ports_to_remove))
    
