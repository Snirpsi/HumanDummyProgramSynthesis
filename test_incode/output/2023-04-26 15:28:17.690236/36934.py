#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds all ports. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <ports>" % sys.argv[0])
        sys.exit()
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        port_number = int(port)
        
        if port_number > 65535:
            print("Port number %s is too large." % port)
            sys.exit()
        
        port_name = port
        
        if port_name == "all":
            port_name = "all"
        
        if port_name == "all":
            port_name = "all"
        
        port_name = port_name.replace("-", "_")
        
        print("Adding port %s" % port_name)
        
        port_number = port_number + 1
        
        port_name = port_name.replace("-", "_")
        
        print("Adding port %s" % port_name)
        
        port_number = port_number + 1
        
        port_name = port_name.replace("-", "_")
        
        print("Adding port %s" % port_name)
        
        port_number = port_number + 1
        
        port_name = port_name.replace("-", "_")
        
        print("Adding port %s" % port_name)
        
        port_number = port_number + 1
        
        port_name = port_name.replace("-", "_")
        
        print("Adding port %s" % port_name)
        
        port_number = port_number + 1
        
        port_name = port_name.replace("-", "_")
        
        print("Adding port %s" % port_name)
        
        port_number = port_number + 1
        
        port_name = port_name.replace("-", "_")
        
        print("Adding port %s" % port_name)
        
        port_number = port_number + 1
        
        port_name = port_name.replace("-", "_")
        
        print("Adding port %s" % port_name)
        
        port_number = port_number + 1
        
        port_name = port_name.replace("-", "_")
        
        print("Adding port %s" % port_name)
        
        port_number = port_number + 1
        
        port_name = port_name.replace("-", "_")
        
        print("Adding port %s" % port_name)
        
        port_number = port_number + 1
        
        port_name = port_name.replace("-", "_")
        
        print("Adding port %s" % port_name)
        
        port_number = port_number + 1
        
        port_name = port_name.replace("-", "_")
        
        print("Adding port %s" % port_name)
        
        port_number = port_number + 1
        
        port_name = port_name.replace("-", "_")
        
        print("Adding port %s" % port_name)
        
        port_number = port_number + 1
        
        port_name = port_name.replace("-", "_")
        