#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports and opens words. """    
    
    # Open port and enumerate all words on that port
    port = 'COM1'
    
    words = []
    
    try:
        # Open port and enumerate all words on that port
        ser = serial.Serial(port, 9600, timeout=1)
        
        while True:
            
            # Read word from serial port
            word = ser.readline()
            
            # Append word to words list
            words.append(word)
            
            # Print word if word is not empty
            if word != '':
                
                # Print word on screen
                sys.stdout.write(word + '\n')
                
    except serial.serialutil.SerialException:
        print('Port {} not open'.format(port))
        
    # Close serial port
    ser.close()
    
    # Print words list
    print('\n'.join(words))
    
