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

    #Re-arrange the values according to the new scoring system you set up. To make things simple, stick with 2, -1, -2, and -3 for values.
    if n == "Transgender Peoples' Rights in the Military":
        if article4engage == 0:
            article4score = 2
        elif article4engage == 1:
            article4score = -1
        elif article4engage == 2:
            article4score = -2
        elif article4engage == 3:
            article4score = -3
        else:
            print("Something is wrong!!")
        return article4score

    #Re-arrange the values according to the new scoring system you set up. To make things simple, stick with -2, 1, 2, and 3 for values.
    if n == "Millenials: Ungrateful, Lazy, Tanking Our Economy":
        if article4engage == 0:
            article4score = -2
        elif article4engage == 1:
            article4score = 1
        elif article4engage == 2:
            article4score = 2
        elif article4engage == 3:
            article4score = 3
        else:
            print("Something is wrong!!")
        return article4score
   
    #Right now, each engagement score leads to a randomized post score between -2 and 2. Feel free to change the random range by changing the numbers inside the parentheses in lines 63, 65, 67, and 69. 
    #If feeling adventurous, instead of changing the random range, you can try to copy lines 47-55 and create different scores.
    if n == "These 10 Tips Will Get You The Job, Number 7 Will SHOCK You":
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

