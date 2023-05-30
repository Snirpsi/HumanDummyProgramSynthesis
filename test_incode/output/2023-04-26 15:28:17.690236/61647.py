#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or opens fruits. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    if len(words) == 0:
        words = ['apple', 'orange', 'banana', 'grape', 'pineapple', 'peach', 'cherry', 'watermelon', 'strawberry', 'mango', 'lemon', 'banana', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banana', 'mango', 'lemon', 'strawberry', 'apple', 'banan