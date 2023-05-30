#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port and adds a list of words. """    
    port = int(sys.argv[1])
    words = []
    
    # Open a socket to listen on the port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    # Accept a connection and then send some data
    while True:
        conn, addr = sock.accept()
        conn.sendall('HTTP/1.1 200 OK\r\n\r\n' + words[0] + '\r\n\r\n')
        conn.close()
        
        # Read all data sent by the client
        data = conn.recv(4096)
        
        # Append the received data to the list of words
        words.append(data)
        
        # Send the list of words to the client
        conn.sendall('HTTP/1.1 200 OK\r\n\r\n' + words[0] + '\r\n\r\n')
        
        # Close the connection
        conn.close()
        
        # Wait a little bit before sending another request
        time.sleep(0.1)
        
    # Close the socket
    sock.close()
    
    # Send a 200 response to the client
    conn.sendall('HTTP/1.1 200 OK\r\n\r\n' + words[0] + '\r\n\r\n')
    
    # Close the connection
    conn.close()
    
    # Wait a little bit before sending another request
    time.sleep(0.1)
    
    # Close the socket
    sock.close()
    
    # Send a 200 response to the client
    conn.sendall('HTTP/1.1 200 OK\r\n\r\n' + words[0] + '\r\n\r\n')
    
    # Close the connection
    conn.close()
    
    # Wait a little bit before sending another request
    time.sleep(0.1)
    
    # Close the socket
    sock.close()
    
    # Send a 200 response to the client
    conn.sendall('HTTP/1.1 200 OK\r\n\r\n' + words[0] + '\r\n\r\n')
    
    # Close the connection
    conn.close()
    
    # Wait a little bit before sending another request
    time.sleep(0.1)
    
    # Close the socket
    sock.close()
    
    # Send a 200 response to the client
    conn.sendall('HTTP/1.1 200 OK\r\n\r\n' + words[0] + '\r\n\r\n')
    
    # Close the connection
    conn.close()
    
    # Wait a little bit before sending another request
    time.sleep(0.1)
    
    # Close the socket
    sock.close()
    
    # Send a 200 response to the client
    conn.sendall('HTTP/1.1 200 OK\r\n\r\n' + words[0] + '\r\n\r\n')
    
    # Close the connection
    conn.close()
    
    # Wait a little bit before sending 