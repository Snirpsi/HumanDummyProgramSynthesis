#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port. """    
    
    # Get the port
    port = input("Enter the port to remove (1-65535): ")
    
    # Get the IP address
    ipaddr = input("Enter the IP address to remove (ex: 192.168.1.1): ")
    
    # Get the mask
    mask = input("Enter the mask to remove (ex: 255.255.255.0): ")
    
    # Get the IP address
    ipaddr = ipaddr.split('.')
    
    # Get the mask
    mask = mask.split('.')
    
    # Remove IP
    ipaddr[0] = int(ipaddr[0]) - int(mask[0])
    ipaddr[1] = int(ipaddr[1]) - int(mask[1])
    ipaddr[2] = int(ipaddr[2]) - int(mask[2])
    
    # Remove mask
    ipaddr[3] = int(ipaddr[3]) - int(mask[3])
    
    # Remove port
    ipaddr[4] = int(ipaddr[4]) - int(port)
    
    # Remove IP address
    ipaddr[5] = int(ipaddr[5]) - int(ipaddr[4])
    
    # Remove IP address
    ipaddr[6] = int(ipaddr[6]) - int(ipaddr[5])
    
    # Remove IP address
    ipaddr[7] = int(ipaddr[7]) - int(ipaddr[6])
    
    # Remove IP address
    ipaddr[8] = int(ipaddr[8]) - int(ipaddr[7])
    
    # Remove IP address
    ipaddr[9] = int(ipaddr[9]) - int(ipaddr[8])
    
    # Remove IP address
    ipaddr[10] = int(ipaddr[10]) - int(ipaddr[9])
    
    # Remove IP address
    ipaddr[11] = int(ipaddr[11]) - int(ipaddr[10])
    
    # Remove IP address
    ipaddr[12] = int(ipaddr[12]) - int(ipaddr[11])
    
    # Remove IP address
    ipaddr[13] = int(ipaddr[13]) - int(ipaddr[12])
    
    # Remove IP address
    ipaddr[14] = int(ipaddr[14]) - int(ipaddr[13])
    
    # Remove IP address
    ipaddr[15] = int(ipaddr[15]) - int(ipaddr[14])
    
    # Remove IP address
    ipaddr[16] = int(ipaddr[16]) - int(ipaddr[15])
    
    # Remove IP address
    ipaddr[17] = int(ipaddr[17]) - int(ipaddr[16])
    
    # Remove IP 