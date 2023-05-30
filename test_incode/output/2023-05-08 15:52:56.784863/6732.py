#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that returns user input.
    web = web.Application([
        (r'/', MainHandler),
    ])
    web.listen(8888)
    print('Listening on port 8888')
    web.run()

