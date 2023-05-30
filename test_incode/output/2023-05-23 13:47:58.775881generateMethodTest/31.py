#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that opens all ports.
    def open_ports():
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            print('Port {} is open'.format(port))
            sock.close()
    open_ports()
    #A function that closes all ports.
    def close_ports():
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            print('Port {} is open'.format(port))
            sock.close()
    close_ports()
    #A function that opens one port and closes it.
    def open_and_close_port():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', ports[0]))
        sock.listen(1)
        print('Port {} is open'.format(ports[0]))
        sock.close()
    open_and_close_port()
    #A function that opens one port and closes it.
    def open_and_close_port_with_timeout():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', ports[0]))
        sock.listen(1)
        print('Port {} is open'.format(ports[0]))
        sock.close()
    open_and_close_port_with_timeout()
    #A function that opens one port and closes it.
    def open_and_close_port_with_timeout_and_timeout():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', ports[0]))
        sock.listen(1)
        print('Port {} is open'.format(ports[0]))
        sock.close()
    open_and_close_port_with_timeout_and_timeout()
    #A function that opens one port and closes it.
    def open_and_close_port_with_timeout_and_timeout_and_timeout():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', ports[0]))
        sock.listen(1)
        print('Port {} is open'.format(ports[0]))
        sock.close()
    open_and_close_port_with_timeout_and_timeout_and_timeout()
    #A function that opens one port and closes it.
    def open_and_close_port_with_timeout_and_timeout_and_timeout_and_timeout():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', ports[0]))
        sock.listen(1)
        print('Port {} is open'.format(ports[0]))
        sock.close()
    open_and_close_port_with_timeout_and_timeout_and_timeout_and_timeout()
    #A function that opens one port and closes it.
    def open_and_close_port_with_timeout_and_timeout_and_timeout_and_timeout_and_timeout():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', ports[0]))
        sock.listen(1)
        print('Port {} is open'.format(ports[0]))
        sock.close()
    open_and_close_port_with_timeout_and_timeout_and_timeout_and_timeout_and_timeout()
    #A function that opens one port and closes it.
    def open_and_close_port_with_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', ports[0]))
        sock.listen(1)
        print('Port {} is open'.format(ports[0]))
        sock.close()
    open_and_close_port_with_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout()
    #A function that opens one port and closes it.
    def open_and_close_port_with_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', ports[0]))
        sock.listen(1)
        print('Port {} is open'.format(ports[0]))
        sock.close()
    open_and_close_port_with_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout()
    #A function that opens one port and closes it.
    def open_and_close_port_with_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', ports[0]))
        sock.listen(1)
        print('Port {} is open'.format(ports[0]))
        sock.close()
    open_and_close_port_with_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout()
    #A function that opens one port and closes it.
    def open_and_close_port_with_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', ports[0]))
        sock.listen(1)
        print('Port {} is open'.format(ports[0]))
        sock.close()
    open_and_close_port_with_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout()
    #A function that opens one port and closes it.
    def open_and_close_port_with_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout_and_timeout():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', ports[0]))
        sock.listen(1)
        print('Port {} is open'.format(ports[0]))
        sock.close()
    open_and_close_port_with_timeout_and_timeout_and_timeout_