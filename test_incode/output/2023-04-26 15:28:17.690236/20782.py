#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    words = []
    
    # Open a socket and listen for connections.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8080))
    sock.listen(1)
    
    # Accept a connection and make a file-like object out of it.
    while True:
        conn, addr = sock.accept()
        
        # Read a line from the connection and add it to the list.
        line = conn.recv(1024).decode('utf-8')
        words.append(line)
        
        # Close the connection and end the loop.
        conn.close()
        
    # Close the socket and end the loop.
    sock.close()
    
    # Print the list of words.
    print('\n'.join(words))
    
    # Close the socket.
    sock.close()
    
    # Close the server.
    server.socket.close()
    
    # Close the socket.
    socket.close()
    
    # Close the server.
    server.socket.close()
    
    # Close the socket.
    socket.close()
    
    # Close the server.
    server.socket.close()
    
    # Close the socket.
    socket.close()
    
    # Close the server.
    server.socket.close()
    
    # Close the socket.
    socket.close()
    
    # Close the server.
    server.socket.close()
    
    # Close the socket.
    socket.close()
    
    # Close the server.
    server.socket.close()
    
    # Close the socket.
    socket.close()
    
    # Close the server.
    server.socket.close()
    
    # Close the socket.
    socket.close()
    
    # Close the server.
    server.socket.close()
    
    # Close the socket.
    socket.close()
    
    # Close the server.
    server.socket.close()
    
    # Close the socket.
    socket.close()
    
    # Close the server.
    server.socket.close()
    
    # Close the socket.
    socket.close()
    
    # Close the server.
    server.socket.close()
    
    # Close the socket.
    socket.close()
    
    # Close the server.
    server.socket.close()
    
    # Close the socket.
    socket.close()
    
    # Close the server.
    server.socket.close()
    
    # Close the socket.
    socket.close()
    
    # Close the server.
    server.socket.close()
    
    # Close the socket.
    socket.close()
    
    # Close the server.
    server.socket.close()
    
    # Close the socket.
    socket.close()
    
    # Close the server.
    server.socket.close()
    
    # Close the socket.
    