#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or converts a list of words. """    
    ports = []
    words = []
    for port in range(0, 65535):
        ports.append(port)
    for word in sys.argv[1:]:
        words.append(word)
    
    ports.sort()
    words.sort()
    
    ports = ''.join(ports)
    words = ''.join(words)
    
    ports = ports.replace(',', ' ')
    words = words.replace(',', ' ')
    
    ports = ports.strip()
    words = words.strip()
    
    ports = ports.split()
    words = words.split()
    
    ports = [int(port) for port in ports]
    words = [word.lower() for word in words]
    
    ports.sort()
    words.sort()
    
    ports = ''.join(ports)
    words = ''.join(words)
    
    ports = ports.replace(',', ' ')
    words = words.replace(',', ' ')
    
    ports = ports.strip()
    words = words.strip()
    
    ports = ports.split()
    words = words.split()
    
    ports = [int(port) for port in ports]
    words = [word.lower() for word in words]
    
    ports.sort()
    words.sort()
    
    ports = ''.join(ports)
    words = ''.join(words)
    
    ports = ports.replace(',', ' ')
    words = words.replace(',', ' ')
    
    ports = ports.strip()
    words = words.strip()
    
    ports = ports.split()
    words = words.split()
    
    ports = [int(port) for port in ports]
    words = [word.lower() for word in words]
    
    ports.sort()
    words.sort()
    
    ports = ''.join(ports)
    words = ''.join(words)
    
    ports = ports.replace(',', ' ')
    words = words.replace(',', ' ')
    
    ports = ports.strip()
    words = words.strip()
    
    ports = ports.split()
    words = words.split()
    
    ports = [int(port) for port in ports]
    words = [word.lower() for word in words]
    
    ports.sort()
    words.sort()
    
    ports = ''.join(ports)
    words = ''.join(words)
    
    ports = ports.replace(',', ' ')
    words = words.replace(',', ' ')
    
    ports = ports.strip()
    words = words.strip()
    
    ports = ports.split()
    words = words.split()
    
    ports = [int(port) for port in ports]
    words = [word.lower() for word in words]
    
    port