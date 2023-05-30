#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port and removes a port. """    
    
    port = '/dev/ttyUSB0'
    
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('', int(port)))
            sock.listen(1)
            
            conn, addr = sock.accept()
            
            conn.close()
            
        except socket.error as e:
            print(e)
            
