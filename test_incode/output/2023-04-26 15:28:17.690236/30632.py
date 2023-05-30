#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port or removes a list of words. """    
    ports = sys.argv[1:]
    
    if len(ports) == 0: 
        print('Usage: %s [port]' % sys.argv[0])
        sys.exit()
    
    for port in ports:
        remove_port(port)
    
    if len(ports) == 1:
        remove_port(ports[0])
    
    if len(ports) == 2:
        remove_port(ports[0], ports[1])
        
    if len(ports) == 3:
        remove_port(ports[0], ports[1], ports[2])
        
    if len(ports) == 4:
        remove_port(ports[0], ports[1], ports[2], ports[3])
        
    if len(ports) == 5:
        remove_port(ports[0], ports[1], ports[2], ports[3], ports[4])
        
    if len(ports) == 6:
        remove_port(ports[0], ports[1], ports[2], ports[3], ports[4], ports[5])
        
    if len(ports) == 7:
        remove_port(ports[0], ports[1], ports[2], ports[3], ports[4], ports[5], ports[6])
        
    if len(ports) == 8:
        remove_port(ports[0], ports[1], ports[2], ports[3], ports[4], ports[5], ports[6], ports[7])
        
    if len(ports) == 9:
        remove_port(ports[0], ports[1], ports[2], ports[3], ports[4], ports[5], ports[6], ports[7], ports[8])
        
    if len(ports) == 10:
        remove_port(ports[0], ports[1], ports[2], ports[3], ports[4], ports[5], ports[6], ports[7], ports[8], ports[9])
        
    if len(ports) == 11:
        remove_port(ports[0], ports[1], ports[2], ports[3], ports[4], ports[5], ports[6], ports[7], ports[8], ports[9], ports[10])
        
    if len(ports) == 12:
        remove_port(ports[0], ports[1], ports[2], ports[3], ports[4], ports[5], ports[6], ports[7], ports[8], ports[9], ports[10], ports[11])
        
    if len(ports) == 13:
        remove_port(ports[0], ports[1], ports[2], ports[3], ports[4], ports[5], ports[6], ports[7], ports[8], ports[9], ports[10], ports[11], ports[12])
        
    if len(ports) == 14:
        remove_port(ports[0], ports[1], ports[2], ports[3], ports[4], ports[5], ports[6], ports[7], ports[8], ports[9], ports[10], ports[11], ports[12], ports[13])
        
    if len(ports) == 15:
        remove_