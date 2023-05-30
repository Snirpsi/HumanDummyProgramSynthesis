#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that enumerates numbers.
    import sys
    import os
    sys.path.append(os.path.abspath('..'))
    from webserver import app
    app.run(host='0.0.0.0', port=8080)

