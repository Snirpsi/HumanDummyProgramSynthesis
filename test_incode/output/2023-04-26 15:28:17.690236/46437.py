#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    sys.path.append('./')
    import webserver
    webserver.serve(webserver.app, host='0.0.0.0', port=8080)
