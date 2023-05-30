#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port or converts all ports. """    
    
    ports = enumeratePorts()
    
    for port in ports:
        
        portName = port[0]
        
        portNumber = port[1]
        
        portName = portName.replace(' ', '_')
        
        portName = portName.replace('-', '_')
        
        portName = portName.replace('.', '_')
        
        portName = portName.replace(':', '_')
        
        portName = portName.replace(';', '_')
        
        portName = portName.replace(',', '_')
        
        portName = portName.replace(';', '_')
        
        portName = portName.replace(':', '_')
        
        portName = portName.replace('-', '_')
        
        portName = portName.replace('_', '_')
        
        portName = portName.replace('~', '_')
        
        portName = portName.replace('!', '_')
        
        portName = portName.replace('@', '_')
        
        portName = portName.replace('#', '_')
        
        portName = portName.replace('$', '_')
        
        portName = portName.replace('%', '_')
        
        portName = portName.replace('^', '_')
        
        portName = portName.replace('&', '_')
        
        portName = portName.replace('*', '_')
        
        portName = portName.replace('(', '_')
        
        portName = portName.replace(')', '_')
        
        portName = portName.replace('{', '_')
        
        portName = portName.replace('}', '_')
        
        portName = portName.replace('|', '_')
        
        portName = portName.replace('}', '_')
        
        portName = portName.replace('<', '_')
        
        portName = portName.replace('>', '_')
        
        portName = portName.replace('?', '_')
        
        portName = portName.replace('@', '_')
        
        portName = portName.replace('#', '_')
        
        portName = portName.replace('$', '_')
        
        portName = portName.replace('%', '_')
        
        portName = portName.replace('^', '_')
        
        portName = portName.replace('&', '_')
        
        portName = portName.replace('*', '_')
        
        portName = portName.replace('(', '_')
        
        portName = portName.replace(')', '_')
        
        portName = portName.replace('{', '_')
        
        portName = portName.replace('}', '_')
        
        portName = portName.replace('|', '_