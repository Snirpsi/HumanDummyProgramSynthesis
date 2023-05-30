#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that removes fruits.
    #The server will listen on port 8000, and will accept connections from
    #any client on that port.
    server = HTTPServer(('', 8000), FruitHandler)
    server.serve_forever()

