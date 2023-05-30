#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    # Get the words from the database
    with sqlite3.connect('words.txt') as db:
        words = db.execute('SELECT word FROM word