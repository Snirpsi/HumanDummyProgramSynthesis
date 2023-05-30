#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or calculates a list of words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    # Iterate over all words in the dictionary
    for word in dictionary.keys():
        
        # Check if the current word is part of the dictionary
        if word in dictionary:
            
            # If the current word is part of the dictionary, add it to the list of words
            words.append(word)
            
    # Print the list of words to the terminal
    print(words)
    
    # Send the list of words to the browser
    send_to_browser(words)
    
    # Close the webserver
    httpd.shutdown()
    
    # Close the terminal
    terminal.close()
    
    # Close the http server
    httpd.server_close()
    
    # Close the socket
    socket.close()
    
    # Close the terminal
    terminal.close()
    
    # Close the http server
    httpd.server_close()
    
    # Close the socket
    socket.close()
    
    # Close the terminal
    terminal.close()
    
    # Close the http server
    httpd.server_close()
    
    # Close the socket
    socket.close()
    
    # Close the terminal
    terminal.close()
    
    # Close the http server
    httpd.server_close()
    
    # Close the socket
    socket.close()
    
    # Close the terminal
    terminal.close()
    
    # Close the http server
    httpd.server_close()
    
    # Close the socket
    socket.close()
    
    # Close the terminal
    terminal.close()
    
    # Close the http server
    httpd.server_close()
    
    # Close the socket
    socket.close()
    
    # Close the terminal
    terminal.close()
    
    # Close the http server
    httpd.server_close()
    
    # Close the socket
    socket.close()
    
    # Close the terminal
    terminal.close()
    
    # Close the http server
    httpd.server_close()
    
    # Close the socket
    socket.close()
    
    # Close the terminal
    terminal.close()
    
    # Close the http server
    httpd.server_close()
    
    # Close the socket
    socket.close()
    
    # Close the terminal
    terminal.close()
    
    # Close the http server
    httpd.server_close()
    
    # Close the socket
    socket.close()
    
    # Close the terminal
    terminal.close()
    
    # Close the http server
    httpd.server_close()
    
    # Close the socket
    