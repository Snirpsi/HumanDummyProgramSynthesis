#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports or removes a list of words. """    
    ports = openports()
    removelist = ["iptables", "iptables-save"]
    
    for port in ports:
        if port in removelist:
            remove(port)
        else:
            add(port)
    
    
<|/ file source=github |>