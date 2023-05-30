#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that adds ports.
    server = HTTPServer(('', 0), Handler)
    for port in ports:
        server.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.socket.bind(('0.0.0.0', port))
        server.socket.listen(1)
    print("Listening on ports " + str(ports))
    server.serve_forever()

