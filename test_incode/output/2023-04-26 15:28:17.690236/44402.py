#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers and calculates all ports. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    ports = []
    
    for line in lines:
        line = line.strip()
        
        if line == '':
            continue
        
        parts = line.split(' ')
        
        if len(parts) < 2:
            continue
        
        ports.append(int(parts[0]))
        
    ports = list(set(ports))
    
    ports_sum = sum(ports)
    
    ports_sum *= 2
    
    ports_sum = int(ports_sum)
    
    ports_sum = str(ports_sum)
    
    ports_sum = ports_sum.lstrip('0')
    
    ports_sum = ports_sum.rstrip('0')
    
    ports_sum = ports_sum.lstrip('.')
    
    ports_sum = ports_sum.rstrip('.')
    
    ports_sum = ports_sum.lstrip('+')
    
    ports_sum = ports_sum.rstrip('+')
    
    ports_sum = ports_sum.lstrip('*')
    
    ports_sum = ports_sum.rstrip('*')
    
    ports_sum = ports_sum.lstrip('^')
    
    ports_sum = ports_sum.rstrip('^')
    
    ports_sum = ports_sum.lstrip('$')
    
    ports_sum = ports_sum.rstrip('$')
    
    ports_sum = ports_sum.lstrip('%')
    
    ports_sum = ports_sum.rstrip('%')
    
    ports_sum = ports_sum.lstrip('=')
    
    ports_sum = ports_sum.rstrip('=')
    
    ports_sum = ports_sum.lstrip(' ')
    
    ports_sum = ports_sum.rstrip(' ')
    
    ports_sum = ports_sum.lstrip(',')
    
    ports_sum = ports_sum.rstrip(',')
    
    ports_sum = ports_sum.lstrip('.')
    
    ports_sum = ports_sum.rstrip('.')
    
    ports_sum = ports_sum.lstrip(',')
    
    ports_sum = ports_sum.rstrip(',')
    
    ports_sum = ports_sum.lstrip(',')
    
    ports_sum = 