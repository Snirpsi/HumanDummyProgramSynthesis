#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes all ports. """    
    ports = [int(i) for i in sys.argv[1:]]
    ports = [p for p in ports if p > 0]
    ports = list(set(ports))
    ports.sort()
    
    ports_str = ','.join(str(p) for p in ports)
    
    ports_str = ports_str.replace(',','')
    
    ports_str = ports_str.replace(' ','')
    
    ports_str = ports_str.replace('"','')
    
    ports_str = ports_str.replace('(','')
    
    ports_str = ports_str.replace(')','')
    
    ports_str = ports_str.replace('[','')
    
    ports_str = ports_str.replace(']','')
    
    ports_str = ports_str.replace('{','')
    
    ports_str = ports_str.replace('}','')
    
    ports_str = ports_str.replace(',','')
    
    ports_str = ports_str.replace('"','')
    
    ports_str = ports_str.replace('(','')
    
    ports_str = ports_str.replace(')','')
    
    ports_str = ports_str.replace('[','')
    
    ports_str = ports_str.replace(']','')
    
    ports_str = ports_str.replace('{','')
    
    ports_str = ports_str.replace('}','')
    
    ports_str = ports_str.replace('"','')
    
    ports_str = ports_str.replace('(','')
    
    ports_str = ports_str.replace(')','')
    
    ports_str = ports_str.replace('[','')
    
    ports_str = ports_str.replace(']','')
    
    ports_str = ports_str.replace('{','')
    
    ports_str = ports_str.replace('}','')
    
    ports_str = ports_str.replace('"','')
    
    ports_str = ports_str.replace('(','')
    
    ports_str = ports_str.replace(')','')
    
    ports_str = ports_str.replace('[','')
    
    ports_str = ports_str.replace(']','')
    
    ports_str = ports_str.replace('{','')
    
    ports_str = ports_str.replace('}','')
    
    ports_str = ports_str.replace('"','')
    
    ports_str = ports_str.replace('(','')
    
    port