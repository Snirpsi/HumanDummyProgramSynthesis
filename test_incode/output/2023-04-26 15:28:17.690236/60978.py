#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits or stores a list of words. """    
    
    import os
    import sys
    import webbrowser
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    
    from app import app
    
    port = int(os.environ.get('PORT', 5000))
    
    webbrowser.open_new('http://127.0.0.1:%d/' % port)
    
    app.run(host='127.0.0.1', port=port)
    
