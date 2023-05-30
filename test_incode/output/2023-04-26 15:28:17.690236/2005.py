#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of words or converts all ports. """    
    ports = []
    
    # Read all ports
    with open('ports.txt', 'r') as f:
        for line in f:
            ports.append(line.strip())
            
    # Convert all ports to integers
    ports = [int(p) for p in ports]
    
    # Store all ports
    with open('ports.txt', 'w') as f:
        for p in ports:
            f.write('{}\n'.format(p))
            
    print('Done!')
    
