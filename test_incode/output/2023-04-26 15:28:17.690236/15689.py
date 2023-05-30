#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports or enumerates a list of words. """    
    ports = [int(i) for i in sys.argv[1:]]
    
    for port in ports:
        
        port_name = str(port)
        
        port_name = port_name.replace(' ', '_')
        
        port_name = port_name.replace('-', '_')
        
        port_name = port_name.replace('_', ' ')
        
        port_name = port_name.replace('.', '_')
        
        port_name = port_name.replace('+', '_')
        
        port_name = port_name.replace('=', '_')
        
        port_name = port_name.replace('(', '_')
        
        port_name = port_name.replace(')', '_')
        
        port_name = port_name.replace(',', '_')
        
        port_name = port_name.replace(':', '_')
        
        port_name = port_name.replace(';', '_')
        
        port_name = port_name.replace('?', '_')
        
        port_name = port_name.replace('!', '_')
        
        port_name = port_name.replace('@', '_')
        
        port_name = port_name.replace('#', '_')
        
        port_name = port_name.replace('$', '_')
        
        port_name = port_name.replace('%', '_')
        
        port_name = port_name.replace('^', '_')
        
        port_name = port_name.replace('&', '_')
        
        port_name = port_name.replace('*', '_')
        
        port_name = port_name.replace('(', '_')
        
        port_name = port_name.replace(')', '_')
        
        port_name = port_name.replace(',', '_')
        
        port_name = port_name.replace(':', '_')
        
        port_name = port_name.replace(';', '_')
        
        port_name = port_name.replace('?', '_')
        
        port_name = port_name.replace('!', '_')
        
        port_name = port_name.replace('@', '_')
        
        port_name = port_name.replace('#', '_')
        
        port_name = port_name.replace('$', '_')
        
        port_name = port_name.replace('%', '_')
        
        port_name = port_name.replace('^', '_')
        
        port_name = port_name.replace('&', '_')
        
        port_name = port_name.replace('*', '_')
        
        port_name = port_name.replace('(', '_')
        
        port_name = port_name.replace(')', '_')
        
        port_name = port_name.replace(',', '_')
        
        port_name = port_name.replace(':', '_')
        
        port_name = port_name.replace(';', '_')
        
        port_name = port_name.replace('?', '_')
        
        port_name = 