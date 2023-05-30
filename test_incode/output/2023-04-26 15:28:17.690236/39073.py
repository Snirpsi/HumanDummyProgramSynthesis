#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits or multiplyes fruits. """    
    
    import os
    import sys
    
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    
    from webserver import app
    
    app.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)
