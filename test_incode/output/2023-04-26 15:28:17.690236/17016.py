#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words. """    
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    words = ' '.join(words)
    words = words.split()
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in punctuation]
    
    words = [word for word in words if word not in numbers]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in punctuation]
    
    words = [word for word in words if word not in numbers]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in punctuation]
    
    words = [word for word in words if word not in numbers]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in punctuation]
    
    words = [word for word in words if word not in numbers]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in punctuation]
    
    words = [word for word in words if word not in numbers]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in punctuation]
    
    words = [word for word in words if word not in numbers]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in punctuation]
    
    words = [word for word in words if word not in numbers]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in stopwords]