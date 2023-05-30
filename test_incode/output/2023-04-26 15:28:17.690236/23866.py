#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or opens user input. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = input("Enter words: ")
    
    if len(words) == 0:
        print("No words entered.")
    else:
        words = [word.strip() for word in words.split(" ")]
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in words if word not in STOPWORDS]
    
    words = [word for word in word