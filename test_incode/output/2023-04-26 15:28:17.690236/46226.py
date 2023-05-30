#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port or removes fruits. """    
    
    ports = [
        port for port in os.listdir('/dev/tty') if port.isdigit()
    ]
    
    while True:
        for port in ports:
            
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((port, 0))
                s.shutdown(2)
                s.close()
            except socket.error:
                pass
            
        ports = [
            port for port in os.listdir('/dev/tty') if port.isdigit()
        ]
        
        time.sleep(1)
        
