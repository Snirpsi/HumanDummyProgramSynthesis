#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that returns words.
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
    from webserver import app
    app.run(host='0.0.0.0', port=8000)

