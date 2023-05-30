#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates user input or converts words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = input("Enter words: ")
    
    words = [word.lower() for word in words.split()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in punctuations]
    
    words = [word for word in words if word not in numbers]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in numbers]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in letters]
    
    words = [