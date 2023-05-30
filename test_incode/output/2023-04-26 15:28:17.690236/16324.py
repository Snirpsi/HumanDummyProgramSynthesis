#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and removes words. """    
    ports = [int(p) for p in sys.argv[1:]]
    ports = list(set(ports))
    ports.sort()
    
    ports_str = ','.join(str(p) for p in ports)
    
    ports_str = ports_str.replace(',','')
    
    ports_str = ports_str.replace('"','')
    
    ports_str = ports_str.replace(':','')
    
    ports_str = ports_str.replace('-','')
    
    ports_str = ports_str.replace('.','')
    
    ports_str = ports_str.replace(';','')
    
    ports_str = ports_str.replace(':','')
    
    ports_str = ports_str.replace('-','')
    
    ports_str = ports_str.replace('.','')
    
    ports_str = ports_str.replace(';','')
    
    ports_str = ports_str.replace(':','')
    
    ports_str = ports_str.replace('-','')
    
    ports_str = ports_str.replace('.','')
    
    ports_str = ports_str.replace(';','')
    
    ports_str = ports_str.replace(':','')
    
    ports_str = ports_str.replace('-','')
    
    ports_str = ports_str.replace('.','')
    
    ports_str = ports_str.replace(';','')
    
    ports_str = ports_str.replace(':','')
    
    ports_str = ports_str.replace('-','')
    
    ports_str = ports_str.replace('.','')
    
    ports_str = ports_str.replace(';','')
    
    ports_str = ports_str.replace(':','')
    
    ports_str = ports_str.replace('-','')
    
    ports_str = ports_str.replace('.','')
    
    ports_str = ports_str.replace(';','')
    
    ports_str = ports_str.replace(':','')
    
    ports_str = ports_str.replace('-','')
    
    ports_str = ports_str.replace('.','')
    
    ports_str = ports_str.replace(';','')
    
    ports_str = ports_str.replace(':','')
    
    ports_str = ports_str.replace('-','')
    
    ports_str = ports_str.replace('.','')
    
    ports_str = ports_str.replace(';','')
    