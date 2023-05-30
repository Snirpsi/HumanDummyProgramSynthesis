#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports. """    
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', 0))
        sock.listen(1)
        sock.close()
        print("Port closed")
        time.sleep(1)
