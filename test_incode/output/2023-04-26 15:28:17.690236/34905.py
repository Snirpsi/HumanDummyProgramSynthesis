#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port. """    
    port = int(sys.argv[1])
    
    # Open a port and read its content
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(('', port))
        sock.listen(1)
        conn, addr = sock.accept()
        data = conn.recv(1024)
        conn.close()
        
        # Send the content
        conn.send(data)
        
        # Close the connection
        conn.close()
        
    # Close the socket
    sock.close()
    
    # 