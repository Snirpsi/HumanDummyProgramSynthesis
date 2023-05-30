#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or opens a list of words. """    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = input("Enter a list of words: ")
    
    words = [word.strip() for word in words.split()]
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if len(word) > 0]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in punctuations]
    
    words = [word for word in words if len(word) > 2]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word not in numbers]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in word