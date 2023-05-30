#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that converts words.txt into words.txt with spaces.
    import sys
    words = [word.strip() for word in open(sys.argv[1])]
    open(sys.argv[2],"w").writelines(" ".join(words))

