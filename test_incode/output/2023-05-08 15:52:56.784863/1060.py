#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that calculates words.
    #It reads words from stdin and prints them out in reverse order.
    words = list(map(str.strip, stdin.read().split()))
    print(" ".join(words[::-1]))

