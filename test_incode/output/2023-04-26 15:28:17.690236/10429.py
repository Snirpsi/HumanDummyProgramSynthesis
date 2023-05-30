#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words and returns a port. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 wordcount.py <filename>")
        sys.exit()
    
    with open(sys.argv[1]) as f:
        words = [word.strip() for word in f]
    
    word_counts = Counter(words)
    
    word_counts_sorted = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    word_counts_sorted = [word for word, count in word_counts_sorted]
    
    word_counts_sorted = [word for word in word_counts_sorted if word.isalpha()]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in stopwords]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in punctuations]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in numbers]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in symbols]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in words]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in words]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in words]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in words]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in words]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in words]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in words]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in words]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in words]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in words]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in words]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in words]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in words]
    
    word_counts_sorted = [word for word in word_counts_sorted if word not in words]
    
    word_count