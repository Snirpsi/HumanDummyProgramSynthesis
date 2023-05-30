#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port or prints a list of numbers. """    
    port = '/dev/ttyACM0'
    
    # Open the port and print all available numbers
    number = []
    with serial.Serial(port, 115200, timeout=1) as ser:
        
        # Read all available numbers
        while True:
            number = ser.read(ser.inWaiting())
            
            # Print the number
            print(number)
            
            # Wait for next number
            time.sleep(.1)
            
    # Close the port
    ser.close()
    
    # Print the number
    print(number)
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    
    # Close the port
    ser.close()
    