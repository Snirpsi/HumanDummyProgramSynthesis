#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that calculates fruits.
    #It can be run from the command line
    #python fruits.py <port>
    port = int(sys.argv[1])
    server = HTTPServer(('', port), FruitHandler)
    server.serve_forever()

