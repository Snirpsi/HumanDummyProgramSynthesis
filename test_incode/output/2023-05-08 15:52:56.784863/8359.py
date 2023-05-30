#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that returns words.
    import sys
    import os
    sys.path.append(os.path.abspath('..'))
    from webserver import app
    app.run(host='0.0.0.0', port=5000)

