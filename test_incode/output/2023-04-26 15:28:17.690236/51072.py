#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates all ports. """    
    ports = []
    
    ports.append({'port': 80, 'name': 'http'})
    ports.append({'port': 443, 'name': 'https'})
    ports.append({'port': 80, 'name': 'http'})
    ports.append({'port': 443, 'name': 'https'})
    
    for port in ports:
        port['port'] = int(port['port'])
        
    ports = sorted(ports, key=lambda k: k['port'])
    
    for port in ports:
        print('Port {} is {}'.format(port['port'], port['name']))
        
