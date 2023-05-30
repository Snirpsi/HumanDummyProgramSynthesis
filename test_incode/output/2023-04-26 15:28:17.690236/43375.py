#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port and enumerates words. """    
    port = 'COM1'
    words = []
    
    ports = serial.tools.list_ports.comports()
    for port in ports:
        port = str(port)
        
        baud = 115200
        
        ser = serial.Serial(port, baud, timeout=1)
        
        ser.flushInput()
        ser.flushOutput()
        
        words = ser.read_until('\n', 1)
        
        words = [word.strip() for word in words.split('\n') if word.strip()]
        
        words = [word for word in words if word]
        
        words = [word for word in words if word.isalpha()]
        
        words = [word for word in words if word.isdigit()]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word for word in words if word not in string.punctuation]
        
        words = [word 