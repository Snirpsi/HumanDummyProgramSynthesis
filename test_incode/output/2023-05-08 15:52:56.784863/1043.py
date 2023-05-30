#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that removes fruits.
    #It also prints the number of fruits removed.
    server = HTTPServer(('', 80), FruitRemover)
    server.serve_forever()

