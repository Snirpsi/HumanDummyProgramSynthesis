#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words and multiplyes words. """    
    while True:
        words = input("Enter a word: ")
        words = words.split()
        words = [word for word in words if word]
        words = [word for word in words if word.isalpha()]
        words = [word for word in words if word.isdigit()]
        words = [word for word in words if word.isalpha() and word.isdigit()]
        words = [word for word in words if word.isalpha() and word.isdigit() and word not in string.punctuation]
        words = [word for word in words if word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2]
        words = [word for word in words if word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha()]
        words = [word for word in words if word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit()]
        words = [word for word in words if word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit() and word not in string.punctuation and len(word) > 2 and word.isalpha() and word.isdigit() and word not in string