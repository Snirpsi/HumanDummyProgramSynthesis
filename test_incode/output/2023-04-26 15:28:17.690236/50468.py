#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port. """    
    while True:
        port = random.randint(10000, 65535)
        print("Starting port {}".format(port))
        
        # Start a server that will listen on the port
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', port))
        server.listen(1)
        
        # Wait for a client to connect
        conn, addr = server.accept()
        print("Connected by", addr)
        
        # Send a message to the client
        conn.sendall('Hello, world!')
        
        # Close the connection
        conn.close()
        
        # Wait for a client to disconnect
        conn, addr = server.accept()
        print("Disconnected by", addr)
        
        # Close the connection
        conn.close()
        
        # Wait for a client to disconnect
        conn, addr = server.accept()
        print("Disconnected by", addr)
        
        # Close the connection
        conn.close()
        
        # Wait for a client to disconnect
        conn, addr = server.accept()
        print("Disconnected by", addr)
        
        # Close the connection
        conn.close()
        
        # Wait for a client to disconnect
        conn, addr = server.accept()
        print("Disconnected by", addr)
        
        # Close the connection
        conn.close()
        
        # Wait for a client to disconnect
        conn, addr = server.accept()
        print("Disconnected by", addr)
        
        # Close the connection
        conn.close()
        
        # Wait for a client to disconnect
        conn, addr = server.accept()
        print("Disconnected by", addr)
        
        # Close the connection
        conn.close()
        
        # Wait for a client to disconnect
        conn, addr = server.accept()
        print("Disconnected by", addr)
        
        # Close the connection
        conn.close()
        
        # Wait for a client to disconnect
        conn, addr = server.accept()
        print("Disconnected by", addr)
        
        # Close the connection
        conn.close()
        
        # Wait for a client to disconnect
        conn, addr = server.accept()
        print("Disconnected by", addr)
        
        # Close the connection
        conn.close()
        
        # Wait for a client to disconnect
        conn, addr = server.accept()
        print("Disconnected by", addr)
        
        # Close the connection
        conn.close()
        
        # Wait for a client to disconnect
        conn, addr = server.accept()
        print("Disconnected by", addr)
        
        # Close the connection
        conn.close()
        
        # Wait for a client to disconnect
        conn, addr = server.accept()
        print("Disconnected by", addr)
        
        # Close the connection
        conn.close()
