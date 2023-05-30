#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers. """    
    import sys
    sys.path.append('./')
    from webserver import app
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
