#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers. """    
    import sys
    import os
    
    sys.path.append(os.getcwd())
    
    from webserver import app
    
    app.run(host='0.0.0.0', port=5000)
