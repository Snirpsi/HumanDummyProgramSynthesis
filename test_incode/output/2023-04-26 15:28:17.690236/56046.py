#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports and multiplyes a port. """    
    
    # Open the port
    port = serial.Serial('/dev/ttyAMA0',115200)
    
    # Iterate over all ports
    for port in serial.tools.list_ports.comports():
        
        # Print the port name
        print('Port name: ' + port.device)
        
        # Open the port and read its contents
        port.open()
        port.close()
        
        # Print the port contents
        print('Port contents:')
        print(port.read())
        
        # Close the port
        port.close()
        
        # Print the port name
        print('Port name: ' + port.device)
        
        # Open the port and write its contents
        port.open()
        port.write('1')
        port.close()
        
        # Print the port contents
        print('Port contents:')
        print(port.read())
        
        # Close the port
        port.close()
        
        # Print the port name
        print('Port name: ' + port.device)
        
        # Open the port and read its contents
        port.open()
        port.write('2')
        port.close()
        
        # Print the port contents
        print('Port contents:')
        print(port.read())
        
        # Close the port
        port.close()
        
        # Print the port name
        print('Port name: ' + port.device)
        
        # Open the port and write its contents
        port.open()
        port.write('3')
        port.close()
        
        # Print the port contents
        print('Port contents:')
        print(port.read())
        
        # Close the port
        port.close()
        
        # Print the port name
        print('Port name: ' + port.device)
        
        # Open the port and read its contents
        port.open()
        port.write('4')
        port.close()
        
        # Print the port contents
        print('Port contents:')
        print(port.read())
        
        # Close the port
        port.close()
        
        # Print the port name
        print('Port name: ' + port.device)
        
        # Open the port and read its contents
        port.open()
        port.write('5')
        port.close()
        
        # Print the port contents
        print('Port contents:')
        print(port.read())
        
        # Close the port
        port.close()
        
        # Print the port name
        print('Port name: ' + port.device)
        
        # Open the port and read its contents
        port.open()
        port.write('6')
        port.close()
        
        # Print the port contents
        print('Port contents:')
        print(port.