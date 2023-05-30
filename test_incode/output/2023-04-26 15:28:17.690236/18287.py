#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits or removes words. """    
    
    # Setup Flask server
    app = Flask(__name__)
    
    # Setup Flask routes
    @app.route('/')
    def index():
        """ Return all fruits or remove a word """
        
        # Return all fruits
        return render_template('index.html')
    
    # Setup Flask routes
    @app.route('/fruits/<string:fruit>')
    def fruits(fruit):
        """ Return a specific fruit """
        
        # Return specific fruit
        return render_template('fruits.html', fruit=fruit)
    
    # Setup Flask routes
    @app.route('/fruits/<string:fruit>/<string:word>')
    def fruits_word(fruit, word):
        """ Return a specific fruit with a specific word """
        
        # Return specific fruit with a specific word
        return render_template('fruits.html', fruit=fruit, word=word)
    
    # Setup Flask routes
    @app.route('/fruits/<string:fruit>/<string:word>/<string:remove>')
    def fruits_word_remove(fruit, word, remove):
        """ Return a specific fruit with a specific word and a specific remove word """
        
        # Return specific fruit with a specific word and a specific remove word
        return render_template('fruits.html', fruit=fruit, word=word, remove=remove)
    
    # Setup Flask routes
    @app.route('/fruits/<string:fruit>/<string:word>/<string:remove>/<string:remove>')
    def fruits_word_remove_word(fruit, word, remove, remove):
        """ Return a specific fruit with a specific word and a specific remove word and a specific remove word """
        
        # Return specific fruit with a specific word and a specific remove word and a specific remove word
        return render_template('fruits.html', fruit=fruit, word=word, remove=remove, remove=remove)
    
    # Setup Flask routes
    @app.route('/fruits/<string:fruit>/<string:word>/<string:remove>/<string:remove>/<string:remove>')
    def fruits_word_remove_word_remove(fruit, word, remove, remove, remove):
        """ Return a specific fruit with a specific word and a specific remove word and a specific remove word and a specific remove word """
        
        # Return specific fruit with a specific word and a specific remove word and a specific remove word and a specific remove word
        return render_template('fruits.html', fruit=fruit, word=word, remove=remove, remove=remove, remove=remove)
    
    # Setup Flask routes
    @app.route('/fruits/<string:fruit>/<string:word>/<string:remove>/<string:remove>/<string:remove>/<string:remove