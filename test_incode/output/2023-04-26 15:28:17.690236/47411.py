#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers or returns all ports. """    
    
    ports = []
    
    # Start a server
    server = HTTPServer(('', 0), MyHandler)
    
    # Start a client and wait for connection
    client_socket = socket.socket()
    client_socket.connect(('localhost', 0))
    
    # Wait for connection
    client_socket.send('GET / HTTP/1.0\r\n\r\n')
    
    # Receive the response
    response = client_socket.recv(1024)
    
    # Close the connection
    client_socket.close()
    
    # Print the response
    print(response)
    
    # Close the server
    server.socket.close()
    
    # Wait for exit
    server.socket.shutdown(socket.SHUT_RDWR)
    server.socket.close()
    
    # Wait for exit
    server.socket.shutdown(socket.SHUT_RDWR)
    server.socket.close()
    
    # Wait for exit
    server.socket.shutdown(socket.SHUT_RDWR)
    server.socket.close()
    
    # Wait for exit
    server.socket.shutdown(socket.SHUT_RDWR)
    server.socket.close()
    
    # Wait for exit
    server.socket.shutdown(socket.SHUT_RDWR)
    server.socket.close()
    
    # Wait for exit
    server.socket.shutdown(socket.SHUT_RDWR)
    server.socket.close()
    
    # Wait for exit
    server.socket.shutdown(socket.SHUT_RDWR)
    server.socket.close()
    
    # Wait for exit
    server.socket.shutdown(socket.SHUT_RDWR)
    server.socket.close()
    
    # Wait for exit
    server.socket.shutdown(socket.SHUT_RDWR)
    server.socket.close()
    
    # Wait for exit
    server.socket.shutdown(socket.SHUT_RDWR)
    server.socket.close()
    
    # Wait for exit
    server.socket.shutdown(socket.SHUT_RDWR)
    server.socket.close()
    
    # Wait for exit
    server.socket.shutdown(socket.SHUT_RDWR)
    server.socket.close()
    
    # Wait for exit
    server.socket.shutdown(socket.SHUT_RDWR)
    server.socket.close()
    
    # Wait for exit
    server.socket.shutdown(socket.SHUT_RDWR)
    server.socket.close()
    
    # Wait for exit
    server.socket.shutdown(socket.SHUT_RDWR)
    server.socket.close()
    
    # Wait for exit
    server.socket.shutdown(socket.SHUT_RDWR)
    server.socket.close()
    
    # Wait for exit
    