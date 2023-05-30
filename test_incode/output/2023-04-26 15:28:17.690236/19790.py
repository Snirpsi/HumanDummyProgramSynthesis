#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
        
    words = ' '.join(words)
    
    words = words.split()
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if len(word) > 2]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in punctuations]
    
    words = [word for word in words if word not in numbers]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if word not in letters]
    
    words = [word for word in words if 