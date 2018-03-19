#see liness 30, 45, and 60 for instructions!

{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}

import random

def fourthpostscore(n):
    article4clicks = int(input("The post above appears. Write in 0 for 'no action,' 1 for 'click to read', or 2 for 'like'"))
    if article4clicks == 0:
        print("You took no action")
    elif article4clicks == 1: 
        print("You clicked the article")
    elif article4clicks == 2:
        print("You clicked on and liked the article")
    else:
        print("That is not a valid response, please enter a valid response")
    
    article4com = int(input("Write in 0 for 'no action,' 1 for 'comment'"))
    if article4com == 0:
        print("You did NOT comment on the article")
    elif article4com == 1:
        print("You commented on the post")
    else:
        print("That is not a valid response, please enter a valid response")
    article4engage = article4clicks + article4com

    #change the scores in the brackets. Right now, if engagement equals 0, then the score is 2; if engagement equals 1, score is -1; if it equals 2, it equals -2; if engagement equals 3, the score becomes -3.
    if n == "Transgender Peoples' Rights in the Military":
        article4listA = [2, -1, -2, -3]
        if article4engage == 0:
            article4score = article4listA[0]
        elif article4engage == 1:
            article4score = article4listA[1]
        elif article4engage == 2:
            article4score = article4listA[2]
        elif article4engage == 3:
            article4score = article4listA[3]
        else:
            print("Something is wrong!!")
        return article4score

    #change the scores in the brackets. Right now, if engagement equals 0, then the score is -2; if engagement equals 1, score is 1; if it equals 2, it equals 2; if engagement equals 3, the score becomes 3.
    if n == "Millenials: Ungrateful, Lazy, Tanking Our Economy":
        article4listC = [-2, 1, 2, 3]
        if article4engage == 0:
            article4score = article4listC[0]
        elif article4engage == 1:
            article4score = article4listC[1]
        elif article4engage == 2:
            article4score = article4listC[2]
        elif article4engage == 3:
            article4score = article4listC[3]
        else:
            print("Something is wrong!!")
        return article4score
   
    #Right now, each engagement score leads to a randomized post score between -2 and 2. Feel free to change the random range by changing the numbers inside the parentheses in lines 63, 65, 67, and 69. 
    #If feeling adventurous, instead of changing the random range, you can try to copy lines 47-55 and create different scores inside the bracket. If you do the latter, make sure you give a new name to "article4listC". You can call it "article4listB," instead.
    if n == "These 10 Tips Save Will Get You The Job, Number 7 Will SHOCK You":
        if article4engage == 0:
            article4score = random.randrange(-2,2)
        elif article4engage == 1:
            article4score = random.randrange(-2,2)
        elif article4engage == 2:
            article4score = random.randrange(-2,2)
        elif article4engage == 3:
            article4score = random.randrange(-2,2)
        else:
            print("Something is wrong!!")
        return article4score

