#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that adds a port.
    port = int(sys.argv[1])
    
    #A function that starts the server.
    httpd = make_server('', port, application)
    httpd.serve_forever()

