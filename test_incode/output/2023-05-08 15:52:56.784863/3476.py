#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that opens a list of numbers.
    web = web.Application([
        (r'/', web.StaticFileHandler, {'path': './'}),
        (r'/numbers', web.StaticFileHandler, {'path': './numbers'}),
        (r'/numbers/([0-9]+)', web.StaticFileHandler, {'path': './numbers/'})
    ])
    web.listen(8080)
    web.run(host='0.0.0.0', port=8080)

