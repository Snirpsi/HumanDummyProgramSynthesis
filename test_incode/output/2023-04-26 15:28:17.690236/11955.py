#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    ports_str = [str(p) for p in ports]
    
    ports_str = ','.join(ports_str)
    
    ports_str = ports_str.replace(',', ';')
    
    ports_str = ports_str.replace('"', '\\"')
    
    ports_str = ports_str.replace('\\', '\\\\')
    
    ports_str = ports_str.replace('\n', '\\n')
    
    ports_str = ports_str.replace('\r', '\\r')
    
    ports_str = ports_str.replace('\t', '\\t')
    
    ports_str = ports_str.replace('"', '\\"')
    
    ports_str = ports_str.replace('\\', '\\\\')
    
    ports_str = ports_str.replace('"', '\\"')
    
    ports_str = ports_str.replace('\\', '\\\\')
    
    ports_str = ports_str.replace('"', '\\"')
    
    ports_str = ports_str.replace('\\', '\\\\')
    
    ports_str = ports_str.replace('"', '\\"')
    
    ports_str = ports_str.replace('\\', '\\\\')
    
    ports_str = ports_str.replace('"', '\\"')
    
    ports_str = ports_str.replace('\\', '\\\\')
    
    ports_str = ports_str.replace('"', '\\"')
    
    ports_str = ports_str.replace('\\', '\\\\')
    
    ports_str = ports_str.replace('"', '\\"')
    
    ports_str = ports_str.replace('\\', '\\\\')
    
    ports_str = ports_str.replace('"', '\\"')
    
    ports_str = ports_str.replace('\\', '\\\\')
    
    ports_str = ports_str.replace('"', '\\"')
    
    ports_str = ports_str.replace('\\', '\\\\')
    
    ports_str = ports_str.replace('"', '\\"')
    
    ports_str = ports_str.replace('\\', '\\\\')
    
    ports_str = ports_str.replace('"', '\\"')
    
    ports_str = ports_str.replace('\\', '\\\\')
    
    ports_str = ports_str.replace('"', '\\"')
    
    ports_str = ports_str.replace('\\', '\\\\')
    
    ports_str = ports_str.replace('"', '\\"')
    
    port