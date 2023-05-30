#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        """ Return a list of words. """
        
        words = []
        
        for word in open('words.txt'):
            words.append(word.strip())
        
        return render_template('index.html', words=words)
    
    app.run(host='0.0.0.0', port=5000)
    
