#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    ports = []
    
    # Start a server
    server = HTTPServer(('', 80), Handler)
    
    # Start a client and wait for connections
    clients = []
    for i in range(0, 10):
        client = HTTPConnection('localhost', 80)
        clients.append(client)
        
    # Wait for connections
    server.serve_forever()
    
    # Close the server
    server.socket.close()
    
    # Close the clients
    for client in clients:
        client.socket.close()
    
    # Print the ports
    for port in ports:
        print('Port {} is open.'.format(port))
    
    # Close the server
    server.socket.close()
    
    # Close the clients
    for client in clients:
        client.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the clients
    for client in clients:
        client.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the clients
    for client in clients:
        client.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the clients
    for client in clients:
        client.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the clients
    for client in clients:
        client.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the clients
    for client in clients:
        client.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the clients
    for client in clients:
        client.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the clients
    for client in clients:
        client.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the clients
    for client in clients:
        client.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the clients
    for client in clients:
        client.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the clients
    for client in clients:
        client.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the clients
    for client in clients:
        client.socket.close()
    
    # Close the server
    server.socket.close()
    
    # Close the clients
    for client in clients:
        client.socket.close()
