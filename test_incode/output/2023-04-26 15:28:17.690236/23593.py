#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or removes all ports. """    
    port = int(sys.argv[1])
    words = []
    
    # Open the port and read all words from it
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.listen(1)
        conn, addr = s.accept()
        
        # Read all words from the connection
        while True:
            data = conn.recv(1024)
            if not data:
                break
            words.append(data.decode())
        
        # Close the connection
        conn.close()
        
    # Return the list of words
    return words

<|/ file ext=.py source=github |>