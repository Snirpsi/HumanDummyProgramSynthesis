#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts a list of words.
    #It will listen on port 8000 and convert each word into lowercase.
    import sys
    import socket
    import os
    
    HOST, PORT = "localhost", 8000
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    
    while True:
        connection, client_address = server_socket.accept()
        
        words = connection.recv(1024).decode()
        words = words.split()
        
        for word in words:
            word = word.lower()
            
            connection.send(word + "\n")
        
        connection.close()
        
    server_socket.close()

