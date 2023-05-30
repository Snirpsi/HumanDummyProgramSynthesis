#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter a filename: ")
    
    file = open(filename, 'r')
    
    words = file.read().split()
    
    file.close()
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in digits]
    
    words = [word for word in words if word not in punctuations]
    
    words = [word for word in words if word not in urls]
    
    words = [word for word in words if word not in emails]
    
    words = [word for word in words if word not in urls]
    
    words = [word for word in words if word not in emails]
    
    words = [word for word in words if word not in urls]
    
    words = [word for word in words if word not in emails]
    
    words = [word for word in words if word not in urls]
    
    words = [word for word in words if word not in emails]
    
    words = [word for word in words if word not in urls]
    
    words = [word for word in words if word not in emails]
    
    words = [word for word in words if word not in urls]
    
    words = [word for word in words if word not in emails]
    
    words = [word for word in words if word not in urls]
    
    words = [word for word in words if word not in emails]
    
    words = [word for word in words if word not in urls]
    
    words = [word for word in words if word not in emails]
    
    words = [word for word in words if word not in urls]
    
    words = [word for word in words if word not in emails]
    
    words = [word for word in words if word not in urls]
    
    words = [word for word in words if word not in emails]
    
    words = [word for word in words if word not in urls]
    
    words = [word for word in words if word not in emails]
    
    words = [word for word in words if word not in urls]
    
    words = [word for word in words if word not in emails]
    
    words = [word for word in words if word not in urls]
    
    words = [word for word in words if word not in emails]
    
    words = [word for word in words if word not in urls]
    
