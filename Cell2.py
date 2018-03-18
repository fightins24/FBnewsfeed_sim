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

    #if brave, and if it really makes sense, you can change the scoring values here. For sake of ease, I would recommend sticking with the random values.
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