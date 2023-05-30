#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that opens a port.
    def open_port(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        return sock
    #A function that closes a port.
    def close_port(sock):
        sock.close()
    #A function that reads a line from the socket.
    def read(sock):
        data, addr = sock.recvfrom(1024)
        return data
    #A function that writes a line to the socket.
    def write(sock, data):
        sock.sendto(data, addr)
    #A function that closes the socket and waits for the next connection.
    def close_and_wait(sock):
        sock.close()
        sock, addr = sock.accept()
        return sock
    #A function that waits for the next connection from the socket.
    def wait_and_connect(sock):
        sock, addr = sock.accept()
        return sock
    #A function that waits for the next connection from the socket.
    def wait_and_connect_and_close(sock):
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        return sock
    #A function that waits for the next connection from the socket.
    def wait_and_connect_and_close_and_wait(sock):
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        return sock
    #A function that waits for the next connection from the socket.
    def wait_and_connect_and_close_and_wait_and_close(sock):
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        return sock
    #A function that waits for the next connection from the socket.
    def wait_and_connect_and_close_and_wait_and_close_and_wait(sock):
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        return sock
    #A function that waits for the next connection from the socket.
    def wait_and_connect_and_close_and_wait_and_close_and_wait_and_close(sock):
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        return sock
    #A function that waits for the next connection from the socket.
    def wait_and_connect_and_close_and_wait_and_close_and_wait_and_close_and_wait(sock):
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        return sock
    #A function that waits for the next connection from the socket.
    def wait_and_connect_and_close_and_wait_and_close_and_wait_and_close_and_wait_and_close(sock):
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        return sock
    #A function that waits for the next connection from the socket.
    def wait_and_connect_and_close_and_wait_and_close_and_wait_and_close_and_wait_and_close_and_wait(sock):
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        return sock
    #A function that waits for the next connection from the socket.
    def wait_and_connect_and_close_and_wait_and_close_and_wait_and_close_and_wait_and_close_and_wait_and_close(sock):
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sock, addr = sock.accept()
        sock.