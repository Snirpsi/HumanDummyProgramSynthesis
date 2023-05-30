#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds all ports. """    
    
    # Open the ports file
    ports = open('/etc/openvswitch/ovs.conf', 'r')
    
    # Read each line of the file
    for line in ports:
        
        # Split each line into its constituent parts
        parts = line.strip().split()
        
        # Append each part to a list
        ports.append(parts)
    
    # Close the file
    ports.close()
    
    # Write the list to a file
    with open('/etc/openvswitch/ovs.conf', 'w') as ports_file:
        
        # Write the list to a file
        ports_file.write('\n'.join(' '.join(part) for part in ports))
    
    # Close the file
    ports.close()
    
    # Print the ports file
    print('\n'.join(' '.join(part) for part in ports))
    
    # Close the ports file
    ports.close()
    
    # Print the ports file
    print('\n'.join(' '.join(part) for part in ports))
    
    # Close the ports file
    ports.close()
    
    # Print the ports file
    print('\n'.join(' '.join(part) for part in ports))
    
    # Close the ports file
    ports.close()
    
    # Print the ports file
    print('\n'.join(' '.join(part) for part in ports))
    
    # Close the ports file
    ports.close()
    
    # Print the ports file
    print('\n'.join(' '.join(part) for part in ports))
    
    # Close the ports file
    ports.close()
    
    # Print the ports file
    print('\n'.join(' '.join(part) for part in ports))
    
    # Close the ports file
    ports.close()
    
    # Print the ports file
    print('\n'.join(' '.join(part) for part in ports))
    
    # Close the ports file
    ports.close()
    
    # Print the ports file
    print('\n'.join(' '.join(part) for part in ports))
    
    # Close the ports file
    ports.close()
    
    # Print the ports file
    print('\n'.join(' '.join(part) for part in ports))
    
    # Close the ports file
    ports.close()
    
    # Print the ports file
    print('\n'.join(' '.join(part) for part in ports))
    
    # Close the ports file
    ports.close()
    
    # Print the ports file
    print('\n'.join(' '