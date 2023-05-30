#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port or opens numbers. """    
    
    # Open a port and multiply it by 2
    port1 = open("/dev/ttyUSB0", O_RDWR)
    port2 = open("/dev/ttyUSB0", O_RDWR)
    port1.write(b"2")
    port2.write(b"2")
    port1.close()
    port2.close()
    
    # Open a port and multiply it by 3
    port1 = open("/dev/ttyUSB0", O_RDWR)
    port2 = open("/dev/ttyUSB0", O_RDWR)
    port1.write(b"3")
    port2.write(b"3")
    port1.close()
    port2.close()
    
    # Open a port and multiply it by 4
    port1 = open("/dev/ttyUSB0", O_RDWR)
    port2 = open("/dev/ttyUSB0", O_RDWR)
    port1.write(b"4")
    port2.write(b"4")
    port1.close()
    port2.close()
    
    # Open a port and multiply it by 5
    port1 = open("/dev/ttyUSB0", O_RDWR)
    port2 = open("/dev/ttyUSB0", O_RDWR)
    port1.write(b"5")
    port2.write(b"5")
    port1.close()
    port2.close()
    
    # Open a port and multiply it by 6
    port1 = open("/dev/ttyUSB0", O_RDWR)
    port2 = open("/dev/ttyUSB0", O_RDWR)
    port1.write(b"6")
    port2.write(b"6")
    port1.close()
    port2.close()
    
    # Open a port and multiply it by 7
    port1 = open("/dev/ttyUSB0", O_RDWR)
    port2 = open("/dev/ttyUSB0", O_RDWR)
    port1.write(b"7")
    port2.write(b"7")
    port1.close()
    port2.close()
    
    # Open a port and multiply it by 8
    port1 = open("/dev/ttyUSB0", O_RDWR)
    port2 = open("/dev/ttyUSB0", O_RDWR)
    port1.write(b"8")
    port2.write(b"8")
    port1.close()
    port2.close()
    
    # Open a port and multiply it by 9
    port1 = open("/dev/ttyUS