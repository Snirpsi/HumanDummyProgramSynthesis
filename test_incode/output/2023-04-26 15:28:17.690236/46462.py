#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    
    import os
    
    port = int(os.getenv('PORT', 5000))
    
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        fruits = ['apple', 'banana', 'cherry']
        return render_template('index.html', fruits=fruits)
    
    app.run(host='0.0.0.0', port=port)
    
