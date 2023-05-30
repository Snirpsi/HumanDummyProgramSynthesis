#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that requests a list of words.
    #It will respond with a JSON object containing all words in the list.
    #The server will also print a message to the console when requested.
    import sys
    import socket
    import time
    import os
    import json
    import requests
    
    #Create a socket to listen for connections.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(1)
    
    #Create a dictionary to store all words and their frequencies.
    word_frequencies = {}
    
    #Create a loop that will continuously listen for connections.
    while True:
        #Accept a connection from the client.
        client_socket, address = server_socket.accept()
        
        #Receive the message from the client.
        message = client_socket.recv(1024).decode()
        
        #Process the message and store it in the dictionary.
        words = message.split()
        for word in words:
            if word not in word_frequencies:
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
        
        #Send the response to the client.
        client_socket.send(json.dumps(word_frequencies))
        client_socket.close()
        
        #Sleep for a second before sending a new request.
        time.sleep(0.5)
    
    #Close the socket.
    server_socket.close()

