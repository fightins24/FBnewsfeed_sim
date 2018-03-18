#go to line 31 for instructions!

{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}

firstscore = {}

def firstpost():
    article1clicks = int(input("The article 'Why We Need Tax Cuts: A Boost for the Middle Class' appears. Write in 0 for 'no action,' 1 for 'click to read', or 2 for 'like'"))
    if article1clicks == 0:
        print("You took no action")
    elif article1clicks == 1: 
        print("You clicked the article")
    elif article1clicks == 2:
        print("You clicked on and liked the article")
    else:
        print("That is not a valid response, please enter a valid response")
    article1com = int(input("Write in 0 for 'no action,' 1 for 'comment'"))
    if article1com == 0:
        print("You did NOT comment on the article")
    elif article1com == 1:
        print("You commented on the post")
    else:
        print("That is not a valid response, please enter a valid response")
    article1engage = article1clicks + article1com
    
    #Re-arrange the values according to the new scoring system you set up. To make things simple, stick with -2, 1, 2, and 3 for values. 
    if article1engage == 0:
        article1score = -2
        
    if article1engage == 1:
        article1score = 1
        
    if article1engage == 2:
        article1score = 2
        
    if article1engage == 3:
        article1score = 3
        
    return article1score

firstscore = firstpost()




