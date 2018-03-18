#go to line 30 for instructions!

{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}

def thirdpost():
    FBevent1clicks = int(input("The event 'Protest for Healthcare Downtown' appears. Write in 0 for 'no action,' 1 for 'click to read', or 2 for 'like'"))
    if FBevent1clicks == 0:
        print("You took no action")
    elif FBevent1clicks == 1: 
        print("You clicked the article")
    elif FBevent1clicks == 2:
        print("You clicked on and liked the article")
    else:
        print("That is not a valid response, please enter a valid response")
    FBevent1com = int(input("Write in 0 for 'no action,' 1 for 'comment'"))
    if FBevent1com == 0:
        print("You did NOT comment on the article")
    elif FBevent1com == 1:
        print("You commented on the post")
    else:
        print("That is not a valid response, please enter a valid response")

    FBevent1engage = FBevent1clicks + FBevent1com

    #Re-arrange the values according to the new scoring system you set up. To make things simple, stick with -2, 1, 2, and 3 for values. 
    if FBevent1engage == 0:
        FBevent1score = 2

    if FBevent1engage == 1:
        FBevent1score = -1

    if FBevent1engage == 2:
        FBevent1score = -2

    if FBevent1engage == 3:
        FBevent1score = -3
        
    return FBevent1score

thirdscore = thirdpost()
