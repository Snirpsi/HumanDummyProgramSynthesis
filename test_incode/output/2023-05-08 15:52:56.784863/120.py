#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that requests ports.
    server = HTTPServer(('', 80), RequestHandler)
    for port in ports:
        server.socket = socket.socket()
        server.socket.bind(('0.0.0.0', port))
        server.socket.listen(5)
        print('Listening on port %s' % port)
    try:
        while True:
            server.handle_request()
    except KeyboardInterrupt:
        pass

