#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that converts a list of numbers.
    #It will run on port 8000.
    import sys
    import os
    sys.path.append(os.path.abspath('..'))
    from webserver import app
    app.run(host='0.0.0.0', port=8000)

