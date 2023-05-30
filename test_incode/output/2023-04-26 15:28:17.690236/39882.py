#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers or removes all ports. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python %s <file> [file]' % sys.argv[0])
        sys.exit()
    
    file = sys.argv[1]
    
    ports = []
    
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            
            if line.startswith('#'):
                continue
            
            ports.append(line)
    
    ports = list(set(ports))
    
    ports.sort()
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
    
    print('')
    
    for port in ports:
        print('#', port)
