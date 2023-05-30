#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that enumerates ports.
    for port in ports:
        listen(port)
    
    #A function that listens to ports.
    def listen(port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', port))
        server_socket.listen(1)
        print('Listening on port {}'.format(port))
        while True:
            connection, client_address = server_socket.accept()
            print('Connected by', client_address)
            connection.send('Hello World!')
            connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.
    def accept(connection):
        data = connection.recv(1024)
        print('Received: "{}"'.format(data))
        connection.send('Bye bye!')
        connection.close()
    
    #A function that accepts a connection and prints it.


