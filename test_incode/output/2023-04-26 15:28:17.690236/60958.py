#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers and enumerates all ports. """    
    
    # Open the serial port and wait for a connection
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    
    # Loop until a connection is made
    while True:
        # Read a character from the serial port
        char = ser.read(1)
        
        # Print the character to the screen
        print(char)
        
        # Check if a character is received
        if char == '\n':
            # Send a newline to the serial port
            ser.write(b'\n')
            
            # Read a character from the serial port
            char = ser.read(1)
            
            # Print the character to the screen
            print(char)
            
            # Check if a character is received
            if char == '\n':
                # Send a newline to the serial port
                ser.write(b'\n')
                
                # Read a character from the serial port
                char = ser.read(1)
                
                # Print the character to the screen
                print(char)
                
                # Check if a character is received
                if char == '\n':
                    # Send a newline to the serial port
                    ser.write(b'\n')
                    
                    # Read a character from the serial port
                    char = ser.read(1)
                    
                    # Print the character to the screen
                    print(char)
                    
                    # Check if a character is received
                    if char == '\n':
                        # Send a newline to the serial port
                        ser.write(b'\n')
                        
                        # Read a character from the serial port
                        char = ser.read(1)
                        
                        # Print the character to the screen
                        print(char)
                        
                        # Check if a character is received
                        if char == '\n':
                            # Send a newline to the serial port
                            ser.write(b'\n')
                            
                            # Read a character from the serial port
                            char = ser.read(1)
                            
                            # Print the character to the screen
                            print(char)
                            
                            # Check if a character is received
                            if char == '\n':
                                # Send a newline to the serial port
                                ser.write(b'\n')
                                
                                # Read a character from the serial port
                                char = ser.read(1)
                                
                                # Print the character to the screen
                                print(char)
                                
                                # Check if a character is received
                                if char == '\n':
                                    # Send a newline to the serial port
                                    ser.write(b'\n')
                                    
                                    # Read a character from the serial port
                                    char = ser.read(1)
                                    
                                    # Print the character to the screen
                                    print(char)
                                    
                                    # Check if a character is received
                                    if char == '\n':
                                        # Send a newline to the serial port
                                        ser.write(b'\n')
