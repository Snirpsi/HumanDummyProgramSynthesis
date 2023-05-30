#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words. """    
    words = input("Enter a list of words: ")
    words = words.split()
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in punctuations]
    
    words = [word for word in words if word not in numbers]
    
    words = [word for word in words if word not in symbols]
    
    words = [word for word in words if word not in english]
    
    words = [word for word in words if word not in french]
    
    words = [word for word in words if word not in german]
    
    words = [word for word in words if word not in italian]
    
    words = [word for word in words if word not in spanish]
    
    words = [word for word in words if word not in portuguese]
    
    words = [word for word in words if word not in spanish]
    
    words = [word for word in words if word not in portuguese]
    
    words = [word for word in words if word not in english]
    
    words = [word for word in words if word not in french]
    
    words = [word for word in words if word not in german]
    
    words = [word for word in words if word not in italian]
    
    words = [word for word in words if word not in spanish]
    
    words = [word for word in words if word not in portuguese]
    
    words = [word for word in words if word not in spanish]
    
    words = [word for word in words if word not in portuguese]
    
    words = [word for word in words if word not in english]
    
    words = [word for word in words if word not in french]
    
    words = [word for word in words if word not in german]
    
    words = [word for word in words if word not in italian]
    
    words = [word for word in words if word not in spanish]
    
    words = [word for word in words if word not in portuguese]
    
    words = [word for word in words if word not in spanish]
    
    words = [word for word in words if word not in portuguese]
    
    words = [word for word in word