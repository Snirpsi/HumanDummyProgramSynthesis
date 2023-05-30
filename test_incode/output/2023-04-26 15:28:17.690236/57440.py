#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words and removes all ports. """    
    while True:
        word = input("Enter a word: ")
        words = word.split()
        words = [word.lower() for word in words]
        words = [word for word in words if word.isalpha()]
        words = [word for word in words if word not in '!@#$%^&*()_+{}[]:;<>,./?-']
        words = [word for word in words if word not in '?']
        words = [word for word in words if word not in '!@#$%^&*()_+{}[]:;<>,./?-']
        words = [word for word in words if word not in '?']
        words = [word for word in words if word not in '!@#$%^&*()_+{}[]:;<>,./?-']
        words = [word for word in words if word not in '?']
        words = [word for word in words if word not in '!@#$%^&*()_+{}[]:;<>,./?-']
        words = [word for word in words if word not in '?']
        words = [word for word in words if word not in '!@#$%^&*()_+{}[]:;<>,./?-']
        words = [word for word in words if word not in '?']
        words = [word for word in words if word not in '!@#$%^&*()_+{}[]:;<>,./?-']
        words = [word for word in words if word not in '?']
        words = [word for word in words if word not in '!@#$%^&*()_+{}[]:;<>,./?-']
        words = [word for word in words if word not in '?']
        words = [word for word in words if word not in '!@#$%^&*()_+{}[]:;<>,./?-']
        words = [word for word in words if word not in '?']
        words = [word for word in words if word not in '!@#$%^&*()_+{}[]:;<>,./?-']
        words = [word for word in words if word not in '?']
        words = [word for word in words if word not in '!@#$%^&*()_+{}[]:;<>,./?-']
        words = [word for word in words if word not in '?']
        words = [word for word in words if word not in '!@#$%^&*()_+{}[]