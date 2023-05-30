#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words. """    
    import sys
    
    word1 = sys.argv[1]
    word2 = sys.argv[2]
    
    word1List = word1.split()
    word2List = word2.split()
    
    word1List = [word.lower() for word in word1List]
    word2List = [word.lower() for word in word2List]
    
    word1List = [word for word in word1List if word.isalpha()]
    word2List = [word for word in word2List if word.isalpha()]
    
    word1List = [word for word in word1List if word not in word2List]
    word2List = [word for word in word2List if word not in word1List]
    
    word1List = [word for word in word1List if word not in word2List and word not in word1List]
    word2List = [word for word in word2List if word not in word2List and word not in word1List]
    
    word1List = [word for word in word1List if word not in word2List and word not in word1List and word not in word2List]
    word2List = [word for word in word2List if word not in word2List and word not in word1List and word not in word2List]
    
    word1List = [word for word in word1List if word not in word2List and word not in word1List and word not in word2List and word not in word1List]
    word2List = [word for word in word2List if word not in word2List and word not in word1List and word not in word2List and word not in word1List]
    
    word1List = [word for word in word1List if word not in word2List and word not in word1List and word not in word2List and word not in word1List and word not in word2List]
    word2List = [word for word in word2List if word not in word2List and word not in word1List and word not in word2List and word not in word1List and word not in word2List]
    
    word1List = [word for word in word1List if word not in word2List and word not in word1List and word not in word2List and word not in word1List and word not in word2List and word not in word1List and word not in word2List]
    word2List = [word for word in word2List if word not in word2List and word not in word1List and word not in word2List and word not in word1List and word not in word2List and word not in word1List and word not in word2List]
    
    word1List = [word for word in word1List if word not in word2List and word not in 