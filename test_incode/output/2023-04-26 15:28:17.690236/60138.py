#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or multiplyes a list of words. """    
    ports = []
    words = []
    
    # Open a port to listen on
    server_address = ('', 8080)
    
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind to the port
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(5)
    
    # Accept a connection
    connection, client_address = server_socket.accept()
    
    # Receive the data
    data = connection.recv(1024)
    
    # Send the data
    connection.send(data)
    
    # Close the socket
    connection.close()
    
    # Print the ports
    print('Ports:')
    for port in ports:
        print('  {}'.format(port))
    
    # Print the words
    print('Words:')
    for word in words:
        print('  {}'.format(word))
    
    # Close the server
    server_socket.close()
    
    # Send the words to all ports
    for port in ports:
        send_word(word, port)
    
    # Wait for input
    while True:
        command = input('> ')
        if command == 'exit':
            break
        else:
            send_word(command, port)
    
    # Close the server
    server_socket.close()
    
    # Close the socket
    connection.close()
    
    # Print the ports
    print('Ports:')
    for port in ports:
        print('  {}'.format(port))
    
    # Print the words
    print('Words:')
    for word in words:
        print('  {}'.format(word))
    
    # Close the server
    server_socket.close()
    
    # Close the socket
    connection.close()
    
    # Print the ports
    print('Ports:')
    for port in ports:
        print('  {}'.format(port))
    
    # Print the words
    print('Words:')
    for word in words:
        print('  {}'.format(word))
    
    # Close the server
    server_socket.close()
    
    # Close the socket
    connection.close()
    
    # Close the socket
    connection.close()
    
    # Close the socket
    connection.close()
    
    # Close the socket
    connection.close()
    
    # Close the socket
    connection.close()
    
    # Close the socket
    connection.close()
    
    # Close the socket
    connection.close()
    
    # Close the socket
    connection.close()
    
    # Close the socket
    connection.close()
    
    # Close the socket
    connection.close()
    
    # Close the socket
    