#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    import os
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    from webserver import app
    
    port = int(sys.argv[1])
    
    app.run(host='0.0.0.0', port=port)
    
