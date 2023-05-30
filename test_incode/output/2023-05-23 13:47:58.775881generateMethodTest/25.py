#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that calculates words.
    import os
    import socket
    import webbrowser
    import sys
    
    HOST, PORT = "localhost", 8080
    
    #Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Bind the socket to the port
    sock.bind((HOST, PORT))
    
    #Listen for incoming connections
    sock.listen(1)
    
    #Wait for a connection
    connection, client_address = sock.accept()
    
    #Receive the message from the client
    message = connection.recv(1024)
    
    #Send the message back to the client
    connection.sendall(message)
    
    #Close the connection
    connection.close()
    
    #Close the socket
    sock.close()
    
    #Open a web browser and navigate to localhost:8080
    webbrowser.open("http://localhost:8080")
    
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for word in words:
        print(word)
        
    #Print the words to the screen
    for 