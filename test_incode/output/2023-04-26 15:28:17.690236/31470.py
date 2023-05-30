#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port or iterates over words. """    
    ports = ['COM1', 'COM2', 'COM3']
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', int(port)))
        sock.listen(1)
        print('Listening on port {}'.format(port))
        while True:
            conn, addr = sock.accept()
            print('Connected by', addr)
            conn.send('Hello, world!\n')
            conn.close()
