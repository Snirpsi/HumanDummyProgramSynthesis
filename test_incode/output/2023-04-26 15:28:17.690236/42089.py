#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words and removes numbers. """    
    while True:
        word = input('Enter a word: ')
        word = word.lower()
        words = word.split()
        words = [word for word in words if word.isalpha()]
        words = [word for word in words if word not in '0123456789']
        words = [word for word in words if word.isdigit()]
        words = [word for word in words if word not in '!@#$%^&*()_+{}[]:;<>,.?/']
        words = [word for word in words if word not in '?!']
        words = [word for word in words if word not in '[]{}']
        words = [word for word in words if word not in '{}[]']
        words = [word for word in words if word not in '()']
        words = [word for word in words if word not in '#']
        words = [word for word in words if word not in '[]']
        words = [word for word in words if word not in '{}']
        words = [word for word in words if word not in '()']
        words = [word for word in words if word not in '#']
        words = [word for word in words if word not in '[]']
        words = [word for word in words if word not in '{}']
        words = [word for word in words if word not in '()']
        words = [word for word in words if word not in '#']
        words = [word for word in words if word not in '[]']
        words = [word for word in words if word not in '{}']
        words = [word for word in words if word not in '()']
        words = [word for word in words if word not in '#']
        words = [word for word in words if word not in '[]']
        words = [word for word in words if word not in '{}']
        words = [word for word in words if word not in '()']
        words = [word for word in words if word not in '#']
        words = [word for word in words if word not in '[]']
        words = [word for word in words if word not in '{}']
        words = [word for word in words if word not in '()']
        words = [word for word in words if word not in '#']
        words = [word for word in words if word not in '[]']
        words = [word for word in words if word not in '{}']
        words = [word for word in words if word not in '()']
        words = [word for word in words if word not in '#']
        words = [word for word in words if word not in 