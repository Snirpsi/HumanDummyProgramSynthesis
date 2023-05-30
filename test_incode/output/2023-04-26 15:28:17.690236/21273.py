#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits or removes a list of words. """    
    
    # Initialize a Flask web server
    app = Flask(__name__)
    
    # Define a route to handle GET requests to /fruits/
    @app.route('/fruits/')
    def fruits():
        """ Return a list of fruit names. """
        fruits = ['apple', 'banana', 'cherry']
        return jsonify(fruits)
    
    # Define a route to handle GET requests to /fruits/<fruit>
    @app.route('/fruits/<fruit>')
    def fruit(fruit):
        """ Return a list of fruit names that contain the given fruit. """
        fruits = ['apple', 'banana', 'cherry']
        if fruit in fruits:
            return jsonify(fruits)
        else:
            return jsonify(fruits)
    
    # Define a route to handle GET requests to /fruits/<fruit>/<word>
    @app.route('/fruits/<fruit>/<word>')
    def fruit(fruit, word):
        """ Return a list of fruit names that contain the given fruit and word. """
        fruits = ['apple', 'banana', 'cherry']
        if fruit in fruits and word in fruits[fruit]:
            return jsonify(fruits[fruit][word])
        else:
            return jsonify(fruits[fruit])
    
    # Define a route to handle GET requests to /fruits/<fruit>/<word>/<word>
    @app.route('/fruits/<fruit>/<word>/<word>')
    def fruit(fruit, word, word):
        """ Return a list of fruit names that contain the given fruit and word. """
        fruits = ['apple', 'banana', 'cherry']
        if fruit in fruits and word in fruits[fruit] and word in fruits[fruit][word]:
            return jsonify(fruits[fruit][word][word])
        else:
            return jsonify(fruits[fruit][word])
    
    # Define a route to handle GET requests to /fruits/<fruit>/<word>/<word>/<word>
    @app.route('/fruits/<fruit>/<word>/<word>/<word>')
    def fruit(fruit, word, word, word):
        """ Return a list of fruit names that contain the given fruit and word. """
        fruits = ['apple', 'banana', 'cherry']
        if fruit in fruits and word in fruits[fruit] and word in fruits[fruit][word] and word in fruits[fruit][word][word]:
            return jsonify(fruits[fruit][word][word])
        else:
            return jsonify(fruits[fruit][word][word])
    
    # Define a route to handle GET requests to /fruits/<fruit>/<word>/<word>/<word>/<word>/<word>/<word>/<word>/<