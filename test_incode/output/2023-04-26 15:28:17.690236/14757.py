#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    import sys
    port = int(sys.argv[1])
    
    from webserver import app
    app.run(host='0.0.0.0', port=port)
