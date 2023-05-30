#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that opens numbers.txt and displays its contents
    web = web.HTTPServer(('', 8080), web.RequestHandler)
    web.serve_forever()

