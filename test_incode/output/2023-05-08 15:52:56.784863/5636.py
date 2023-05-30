#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that calculates fruits.
    server = HTTPServer(('', 8080), FruitCalculator)
    server.serve_forever()

