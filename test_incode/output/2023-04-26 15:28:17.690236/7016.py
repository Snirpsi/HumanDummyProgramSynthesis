#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words or opens a list of words. """    
    
    words = []
    
    # Start a webserver
    httpd = HTTPServer(("", 80), WordsHandler)
    
    # Start a thread to serve the request
    threading.Thread(target=httpd.serve_forever).start()
    
    # Wait until the user closes the window
    httpd.server_close()
    
    # Print the list of words to the user
    print("Words:")
    for word in words:
        print(word)
    
    # Print the list of words to the user
    print("Open Words:")
    for word in words:
        if word[0] == 'open':
            print(word)
    
    # Stop the server
    httpd.server_close()
    
    # Close the server
    httpd.socket.close()
    
    # Close the socket
    httpd.socket.close()
    
    # Stop the server
    httpd.server_close()
    
    # Close the socket
    httpd.socket.close()
    
    # Stop the server
    httpd.server_close()
    
    # Close the socket
    httpd.socket.close()
    
    # Stop the server
    httpd.server_close()
    
    # Close the socket
    httpd.socket.close()
    
    # Stop the server
    httpd.server_close()
    
    # Close the socket
    httpd.socket.close()
    
    # Stop the server
    httpd.server_close()
    
    # Close the socket
    httpd.socket.close()
    
    # Stop the server
    httpd.server_close()
    
    # Close the socket
    httpd.socket.close()
    
    # Stop the server
    httpd.server_close()
    
    # Close the socket
    httpd.socket.close()
    
    # Stop the server
    httpd.server_close()
    
    # Close the socket
    httpd.socket.close()
    
    # Stop the server
    httpd.server_close()
    
    # Close the socket
    httpd.socket.close()
    
    # Stop the server
    httpd.server_close()
    
    # Close the socket
    httpd.socket.close()
    
    # Stop the server
    httpd.server_close()
    
    # Close the socket
    httpd.socket.close()
    
    # Stop the server
    httpd.server_close()
    
    # Close the socket
    httpd.socket.close()
    
    # Stop the server
    httpd.server_close()
    
    # Close the socket
    httpd.socket.close()
    
    # Stop the server
    httpd.server_close()
    
    # Close 