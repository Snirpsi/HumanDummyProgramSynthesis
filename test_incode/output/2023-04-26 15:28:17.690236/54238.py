#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port and iterates over words. """    
    words = []
    port = 'COM1'
    
    # Open a serial port and read from it
    ser = serial.Serial(port, 9600, timeout=1)
    
    # Read one word at a time
    while True:
        word = ser.readline()
        
        # Append the word to the list
        words.append(word)
        
        # Print the word if its length is greater than zero
        if len(word) > 0:
            print(word)
            
        # Sleep for one second
        time.sleep(1)
        
    # Close the serial port
    ser.close()
    
    # Print the final list of words
    print(words)
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the serial port
    ser.close()
    
    # Close the 