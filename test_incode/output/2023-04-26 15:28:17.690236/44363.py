#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s port1 port2" % sys.argv[0])
        sys.exit()
    
    port1 = sys.argv[1]
    port2 = sys.argv[2]
    
    port1_str = str(port1)
    port2_str = str(port2)
    
    port1_int = port1_str[2:]
    port2_int = port2_str[2:]
    
    port1_int = int(port1_int)
    port2_int = int(port2_int)
    
    port1_str = port1_int.to_bytes(1, byteorder='big')
    port2_str = port2_int.to_bytes(1, byteorder='big')
    
    port1_int = port1_int.to_bytes(2, byteorder='big')
    port2_int = port2_int.to_bytes(2, byteorder='big')
    
    port1_str = port1_str + port2_str
    
    port1_str = port1_str[2:]
    
    port1_str = port1_str[::-1]
    
    port1_str = port1_str[2:]
    
    port1_str = port1_str[::-1]
    
    port1_str = port1_str[2:]
    
    port1_str = port1_str[::-1]
    
    port1_str = port1_str[2:]
    
    port1_str = port1_str[::-1]
    
    port1_str = port1_str[2:]
    
    port1_str = port1_str[::-1]
    
    port1_str = port1_str[2:]
    
    port1_str = port1_str[::-1]
    
    port1_str = port1_str[2:]
    
    port1_str = port1_str[::-1]
    
    port1_str = port1_str[2:]
    
    port1_str = port1_str[::-1]
    
    port1_str = port1_str[2:]
    
    port1_str = port1_str[::-1]
    
    port1_str = port1_str[2:]
    
    port1_str = port1_str[::-1]
    
    port1_str = port1_str[2:]
    
    port1_str = port1_str[::-1]
    
    port1_str = port1_str[2:]
    
    port1_str = port1_str[::-1]
    
    port1_str = port1_str[2:]
    
    port1_str = port1_str[::-1]
    
    port1_str = port1_str[2:]
    
    port1_str = port1_str[::-1]
    
    port1_str = port1_str[2:]
    
