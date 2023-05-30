#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports and multiplyes words. """    
    
    # Open ports
    ports = [
        port for port in serial.tools.list_ports.comports()
        if port.device == '/dev/ttyACM0'
    ]
    
    # Iterate over ports
    for port in ports:
        
        # Open serial port
        ser = serial.Serial(port, 115200, timeout=1)
        
        # Read word
        word = ser.readline()
        
        # Write word
        ser.write(word * 2)
        
        # Close serial port
        ser.close()
        
        # Print result
        print(word)
        
        # Close port
        port.close()
        
