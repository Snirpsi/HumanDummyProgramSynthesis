#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or opens fruits. """    
    
    web = web.Application([
        (r'/', MainPage),
        (r'/fruits/', FruitPage),
        (r'/words/', WordPage),
        (r'/about/', AboutPage),
        (r'/contact/', ContactPage),
        (r'/