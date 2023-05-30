#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that returns a list of numbers.
    server = http.server
    port = 8000
    server.serve(app, port)
    server.server_forever()

