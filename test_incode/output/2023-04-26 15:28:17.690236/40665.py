#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port or multiplyes all ports. """    
    while True:
        ports = os.listdir('/sys/class/net/')
        for port in ports:
            if  port.isdigit():
                ports.remove(port)
                port = int(port)
                
        if ports:
            for port in ports:
                subprocess.call(['ip', 'link', 'set', port, 'down'])
                subprocess.call(['ip', 'link', 'set', port, 'up'])
        else:
            subprocess.call(['ip', 'link', 'set', 'lo', 'up'])
            
        time.sleep(1)
        
