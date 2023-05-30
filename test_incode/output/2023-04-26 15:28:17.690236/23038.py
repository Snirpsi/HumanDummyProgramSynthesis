#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or stores user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = input("Enter a word: ")
    
    words = words.split()
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if len(word) > 2]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if len(word) > 0]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word 