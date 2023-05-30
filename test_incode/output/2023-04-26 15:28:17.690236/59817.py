#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    ports = [8080, 8081, 8082]
    ports_str = [str(p) for p in ports]
    ports_str = ','.join(ports_str)
    
    ports_str = ports_str.replace(',', ';')
    ports_str = ports_str.replace('"', '""')
    ports_str = ports_str.replace('(', '[')
    ports_str = ports_str.replace(')', ']')
    ports_str = ports_str.replace('<', '{')
    ports_str = ports_str.replace('>', '}')
    ports_str = ports_str.replace('|', '||')
    ports_str = ports_str.replace(':', ':')
    ports_str = ports_str.replace(';', ';')
    ports_str = ports_str.replace('\n', ' ')
    ports_str = ports_str.replace('\r', ' ')
    
    ports_str = ports_str.replace('"', '')
    ports_str = ports_str.replace('(', '')
    ports_str = ports_str.replace(')', '')
    ports_str = ports_str.replace('<', '')
    ports_str = ports_str.replace('>', '')
    ports_str = ports_str.replace('|', '')
    ports_str = ports_str.replace(':', '')
    
    ports_str = ports_str.replace('"', '')
    ports_str = ports_str.replace('(', '')
    ports_str = ports_str.replace(')', '')
    ports_str = ports_str.replace('<', '')
    ports_str = ports_str.replace('>', '')
    ports_str = ports_str.replace('|', '')
    ports_str = ports_str.replace(':', '')
    
    ports_str = ports_str.replace('"', '')
    ports_str = ports_str.replace('(', '')
    ports_str = ports_str.replace(')', '')
    ports_str = ports_str.replace('<', '')
    ports_str = ports_str.replace('>', '')
    ports_str = ports_str.replace('|', '')
    ports_str = ports_str.replace(':', '')
    
    ports_str = ports_str.replace('"', '')
    ports_str = ports_str.replace('(', '')
    ports_str = ports_str.replace(')', '')
    ports_str = ports_str.replace('<', '')
    ports_str = ports_str.replace('>', '')
    ports_str = ports_str.replace('|', '')
    ports_str = ports_str.replace(':', '')
    
    ports_str = ports_str.replace('"', '')
    ports_str = ports_str.replace('(', '')
    port