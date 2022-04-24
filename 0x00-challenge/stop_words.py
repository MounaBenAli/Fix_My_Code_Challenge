#!/usr/bin/python3
string text: the input text. 

int  k: the threshold occurrence count for a word to be a stop word 

Returns string[]: the list of stop words in order of their first occurrence

def stop_words(text, int k):
    text.split(sep="")

txt = "a mouse is smaller than a dog but a dog is stronger"
k = 3
i = 1
x = txt.split(sep=" ")

y = x.count("dog")

[print(i) for i in x]