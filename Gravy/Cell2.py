#go to line 32 for instructions!

{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}

import random

def secondpost():
    video1clicks = int(input("The video 'Delicious Mac and Cheese OMG, so easy!' appears. Write in 0 for 'no action,' 1 to 'click to read', or 2 to 'like'"))
    if video1clicks == 0:
        print("You took no action")
    elif video1clicks == 1: 
        print("You clicked the article")
    elif video1clicks == 2:
        print("You clicked on and liked the article")
    else:
        print("That is not a valid response, please enter a valid response")
    video1com = int(input("Write in 0 for 'no action,' 1 for 'comment'"))
    if video1com == 0:
        print("You did NOT comment on the article")
    elif video1com == 1:
        print("You commented on the post")
    else:
        print("That is not a valid response, please enter a valid response")

    video1engage = video1clicks + video1com

    #Right now, each engagement score leads to a randomized post score between -2 and 2. If it makes sense to keep these scores random, feel free to change the random range by changing the numbers inside the parentheses in lines 34, 37, 40, and 43.
    #Instead, you could delete all of the "random.range(-2,2)" values and add numeric scores like you did in cell 1.
    if video1engage == 0:
        video1score = random.randrange(-2,2)

    if video1engage == 1:
        video1score = random.randrange(-2,2)

    if video1engage == 2:
        video1score = random.randrange(-2,2)

    if video1engage == 3:
        video1score = random.randrange(-2,2)
    return video1score

secondscore = secondpost()