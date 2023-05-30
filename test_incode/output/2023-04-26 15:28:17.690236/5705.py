#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words. """    
    words = open("words.txt").read().splitlines()
    words = [word.strip() for word in words]
    words = [word for word in words if word]
    words = " ".join(words)
    open("words.txt", "w").write(words)
    print("Words added")
