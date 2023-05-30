#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('usage: python word2vec.py <word>')
        sys.exit(1)
    
    word = sys.argv[1]
    
    vec = gensim.models.Word2Vec.load_word2vec_format(word, binary=False)
    
    print(vec.most_similar(positive=['cat', 'dog'], negative=['cat', 'dog']))
    
