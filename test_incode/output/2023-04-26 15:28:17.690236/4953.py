#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words and converts all ports. """    
    ports = open('ports.txt', 'r').read().splitlines()
    
    for port in ports:
        port_number = port.split(':')
        
        port_number = port_number[0]
        
        port_number = port_number.strip()
        
        port_number = port_number.replace(' ', '')
        
        port_number = int(port_number)
        
        port_number = port_number + 2000
        
        port_number = port_number % 65536
        
        port_number = str(port_number)
        
        port_number = port_number.zfill(2)
        
        port_number = port_number.zfill(4)
        
        port_number = port_number.zfill(6)
        
        port_number = port_number.zfill(8)
        
        port_number = port_number.zfill(10)
        
        port_number = port_number.zfill(12)
        
        port_number = port_number.zfill(14)
        
        port_number = port_number.zfill(16)
        
        port_number = port_number.zfill(18)
        
        port_number = port_number.zfill(20)
        
        port_number = port_number.zfill(22)
        
        port_number = port_number.zfill(24)
        
        port_number = port_number.zfill(26)
        
        port_number = port_number.zfill(28)
        
        port_number = port_number.zfill(30)
        
        port_number = port_number.zfill(32)
        
        port_number = port_number.zfill(34)
        
        port_number = port_number.zfill(36)
        
        port_number = port_number.zfill(38)
        
        port_number = port_number.zfill(40)
        
        port_number = port_number.zfill(42)
        
        port_number = port_number.zfill(44)
        
        port_number = port_number.zfill(46)
        
        port_number = port_number.zfill(48)
        
        port_number = port_number.zfill(50)
        
        port_number = port_number.zfill(52)
        
        port_number = port_number.zfill(54)
        
        port_number = port_number.zfill(56)
        
        port_number = port_number.zfill(58)
        
        port_number = port_number.zfill(60)
        
        port_number = port_number.zfill(62)
        
        port_number = port_number.zfill(64)
        
        port_number = port_number.zfill(66)
        
        port_number = port_number.zfill(68)
        
        port_number = port_number.zfill(70)
        
        port_number = port_number.zfill(72)
        
        