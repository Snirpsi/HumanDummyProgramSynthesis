#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words. """    
    import sys
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words.sort()
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if word[0].isspace()]
    
    words = [word for word in words if word[0].isalpha() and word[0].isdigit()]
    
    words = [word for word in words if word[0].isalpha() and word[0].isupper()]
    
    words = [word for word in words if word[0].isalpha() and word[0].isdigit() and word[0].isspace()]
    
    words = [word for word in words if word[0].isalpha() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isspace()]
    
    words = [word for word in words if word[0].isalpha() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isdigit() and word[0].isspace() and word[0].isalpha() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].is