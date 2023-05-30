#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or prints fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = '80'
    
    web = web.application(urls, globals())
    web.run_simple('localhost', port)
    
