#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words and converts fruits. """    
    import sys
    words = sys.argv[1:]
    words = words.split(',')
    fruits = []
    for word in words:
        fruits.append(word.strip().lower())
    fruits.sort()
    for fruit in fruits:
        if fruit not in ['apple', 'banana', 'orange', 'lemon', 'pear', 'plum', 'raspberry', 'strawberry', 'watermelon', 'grape', 'pineapple', 'mango', 'kiwi', 'lemon', 'banana', 'orange', 'lemon', 'pear', 'plum', 'raspberry', 'strawberry', 'watermelon', 'grape', 'pineapple', 'mango', 'kiwi', 'lemon', 'banana', 'orange', 'lemon', 'pear', 'plum', 'raspberry', 'strawberry', 'watermelon', 'grape', 'pineapple', 'mango', 'kiwi', 'lemon', 'banana', 'orange', 'lemon', 'pear', 'plum', 'raspberry', 'strawberry', 'watermelon', 'grape', 'pineapple', 'mango', 'kiwi', 'lemon', 'banana', 'orange', 'lemon', 'pear', 'plum', 'raspberry', 'strawberry', 'watermelon', 'grape', 'pineapple', 'mango', 'kiwi', 'lemon', 'banana', 'orange', 'lemon', 'pear', 'plum', 'raspberry', 'strawberry', 'watermelon', 'grape', 'pineapple', 'mango', 'kiwi', 'lemon', 'banana', 'orange', 'lemon', 'pear', 'plum', 'raspberry', 'strawberry', 'watermelon', 'grape', 'pineapple', 'mango', 'kiwi', 'lemon', 'banana', 'orange', 'lemon', 'pear', 'plum', 'raspberry', 'strawberry', 'watermelon', 'grape', 'pineapple', 'mango', 'kiwi', 'lemon', 'banana', 'orange', 'lemon', 'pear', 'plum', 'raspberry', 'strawberry', 'watermelon', 'grape', 'pineapple', 'mango', 'kiwi', 'lemon', 'banana', 'orange', 'lemon', 'pear', 'plum', 'raspberry', 'strawberry', 'watermelon', 'grape', 'pineapple', 'mango', 'kiwi', 'lemon', 'banana', 'orange', 'lemon', 'pear', 'plum', 'raspberry', 'strawberry', 'watermelon', 'grape', 'pineapple', 'mango', 'kiwi', 'lemon', 'banana', 'orange', 'lemon', 'pear', 'plum', 'raspb