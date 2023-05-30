#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words and removes numbers. """    
    while True:
        words = []
        words = input("Enter a word: ").split()
        words = [word for word in words if word.isalpha()]
        words = [word for word in words if word not in '0123456789']
        words = [word for word in words if word not in '!@#$%^&*()_+{}[]:;"\'<>,.?/']
        print("\n".join(words))
