#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of numbers or removes all ports. """    
    ports = sys.argv[1:]
    
    if len(ports) == 0: 
        print("Usage: %s <ports>" % sys.argv[0])
        sys.exit()
    
    ports = ports.split(',')
    
    for port in ports:
        
        if port == '':
            print("Usage: %s <ports>" % sys.argv[0])
            sys.exit()
        
        if port == '*':
            ports = ports[1:]
            
        if len(ports) == 0: 
            print("Usage: %s <ports>" % sys.argv[0])
            sys.exit()
        
        port = int(port)
        
        if port < 0 or port > 65535:
            print("Usage: %s <ports>" % sys.argv[0])
            sys.exit()
        
        if port in ports:
            ports.remove(port)
            
    if len(ports) == 0:
        print("Usage: %s <ports>" % sys.argv[0])
        sys.exit()
    
    ports = ','.join(ports)
    
    cmd = "sudo iptables -A INPUT -p tcp --dport %s -j ACCEPT" % ports
    
    subprocess.call(cmd, shell=True)
    
    cmd = "sudo iptables -A OUTPUT -p tcp --sport %s -j ACCEPT" % ports
    
    subprocess.call(cmd, shell=True)
    
    cmd = "sudo iptables -A INPUT -p tcp --dport %s -j ACCEPT" % ports
    
    subprocess.call(cmd, shell=True)
    
    cmd = "sudo iptables -A OUTPUT -p tcp --sport %s -j ACCEPT" % ports
    
    subprocess.call(cmd, shell=True)
    
    cmd = "sudo iptables -A INPUT -p tcp --dport %s -j ACCEPT" % ports
    
    subprocess.call(cmd, shell=True)
    
    cmd = "sudo iptables -A OUTPUT -p tcp --sport %s -j ACCEPT" % ports
    
    subprocess.call(cmd, shell=True)
    
    cmd = "sudo iptables -A INPUT -p tcp --dport %s -j ACCEPT" % ports
    
    subprocess.call(cmd, shell=True)
    
    cmd = "sudo iptables -A OUTPUT -p tcp --sport %s -j ACCEPT" % ports
    
    subprocess.call(cmd, shell=True)
    
    cmd = "sudo iptables -A INPUT -p tcp --dport %s -j ACCEPT" % ports
    
    subprocess.call(cmd, shell=True)
    
    cmd = "sudo iptables -A OUTPUT -p tcp --