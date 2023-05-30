#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits. """    
    
    import os
    import sys
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    from fruits import Fruits
    
    app = Fruits()
    
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
    
