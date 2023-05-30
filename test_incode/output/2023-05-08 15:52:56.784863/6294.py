#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that stores a list of numbers.
    import sys
    import os
    sys.path.append(os.getcwd())
    from webserver import app
    app.run(host='0.0.0.0', port=5000)

