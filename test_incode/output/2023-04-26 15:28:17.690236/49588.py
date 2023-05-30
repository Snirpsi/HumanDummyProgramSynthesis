#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or calculates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    ports = [port]
    
    for i in range(2, len(sys.argv)):
        ports.append(int(sys.argv[i]))
    
    ports.sort()
    
    ports_str = ', '.join(map(str, ports))
    
    print('\n'.join([
        'Serving on port %s...' % ports_str,
        '',
        '