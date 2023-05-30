#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 wordmult.py <word1> <word2> ...")
        sys.exit()
    
    word1 = sys.argv[1]
    word2 = sys.argv[2]
    
    if len(sys.argv) > 3:
        word3 = sys.argv[3]
    
    if len(sys.argv) > 4:
        word4 = sys.argv[4]
    
    word1 = word1.lower()
    word2 = word2.lower()
    
    word3 = word3.lower()
    word4 = word4.lower()
    
    word1 = word1.split()
    word2 = word2.split()
    
    word3 = word3.split()
    word4 = word4.split()
    
    word1 = word1[0]
    word2 = word2[0]
    
    word3 = word3[0]
    word4 = word4[0]
    
    word1 = word1.replace(' ', '')
    word2 = word2.replace(' ', '')
    word3 = word3.replace(' ', '')
    word4 = word4.replace(' ', '')
    
    word1 = word1.replace(',', '')
    word2 = word2.replace(',', '')
    word3 = word3.replace(',', '')
    word4 = word4.replace(',', '')
    
    word1 = word1.replace('.', '')
    word2 = word2.replace('.', '')
    word3 = word3.replace('.', '')
    word4 = word4.replace('.', '')
    
    word1 = word1.replace('?', '')
    word2 = word2.replace('?', '')
    word3 = word3.replace('?', '')
    word4 = word4.replace('?', '')
    
    word1 = word1.replace('!', '')
    word2 = word2.replace('!', '')
    word3 = word3.replace('!', '')
    word4 = word4.replace('!', '')
    
    word1 = word1.replace(':', '')
    word2 = word2.replace(':', '')
    word3 = word3.replace(':', '')
    word4 = word4.replace(':', '')
    
    word1 = word1.replace(';', '')
    word2 = word2.replace(';', '')
    word3 = word3.replace(';', '')
    word4 = word4.replace(';', '')
    
    word1 = word1.replace('?', '')
    word2 = word2.replace('?', '')
    word3 = word3.replace('?', '')
    word4 = word4.replace('?', '')
    
    word1 = word1.replace('!', '')
    word2 = word2.replace('!', '')
    word3 = word3.replace('!', '')
    word4 = word4.replace('!', '')
    
    word1 = 