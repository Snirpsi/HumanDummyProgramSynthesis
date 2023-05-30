#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports or multiplyes a list of words. """    
    while True:
        words = input('Enter a word: ')
        words = words.split()
        words = [word for word in words if word]
        words = [word for word in words if word.isalpha()]
        words = [word for word in words if word.isdigit()]
        words = [word for word in words if word.isalnum()]
        words = [word for word in words if word not in '!@#$%^&*()_+{}[]:;<,./?-']
        words = [word for word in words if word not in '#@$%^&*()_+{}[]:;<,./?-']
        words = [word for word in words if word not in '?!@#$%^&*()_+{}[]:;<,./?-']
        words = [word for word in words if word not in '#@$%^&*()_+{}[]:;<,./?-']
        words = [word for word in words if word not in '?!@#$%^&*()_+{}[]:;<,./?-']
        words = [word for word in words if word not in '#@$%^&*()_+{}[]:;<,./?-']
        words = [word for word in words if word not in '?!@#$%^&*()_+{}[]:;<,./?-']
        words = [word for word in words if word not in '#@$%^&*()_+{}[]:;<,./?-']
        words = [word for word in words if word not in '?!@#$%^&*()_+{}[]:;<,./?-']
        words = [word for word in words if word not in '#@$%^&*()_+{}[]:;<,./?-']
        words = [word for word in words if word not in '?!@#$%^&*()_+{}[]:;<,./?-']
        words = [word for word in words if word not in '#@$%^&*()_+{}[]:;<,./?-']
        words = [word for word in words if word not in '?!@#$%^&*()_+{}[]:;<,./?-']
        words = [word for word in words if word not in '#@$%^&*()_+{}[]:;<,./?-']
        words = [word 