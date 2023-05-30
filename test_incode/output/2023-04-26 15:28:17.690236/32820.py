#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and returns a list of numbers. """    
    port = int(sys.argv[1])
    
    numbers = []
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen(5)
        
        while True:
            conn, addr = s.accept()
            
            number = conn.recv(1024).decode('utf-8')
            
            numbers.append(int(number))
            
            conn.close()
    
    return numbers
