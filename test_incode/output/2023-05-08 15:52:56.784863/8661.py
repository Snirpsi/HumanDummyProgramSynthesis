#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.html and displays them in fruirs.html
    webserver = HTTPServer(('', 8000), FruirsHandler)
    webserver.serve_forever()

