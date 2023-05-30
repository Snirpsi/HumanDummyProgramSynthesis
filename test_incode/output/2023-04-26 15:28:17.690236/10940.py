#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    
    import os
    import sys
    
    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
    
    from fruit import app
    
    port = int(sys.argv[1])
    
    app.run(host='0.0.0.0', port=port)
    
