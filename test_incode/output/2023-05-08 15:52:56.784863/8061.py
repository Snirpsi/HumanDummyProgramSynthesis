#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that removes all ports.
    def cleanPorts():
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.close()
    cleanPorts()

