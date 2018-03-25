#go to line 11 for instructions!

{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}

def fourthpost(n):
    #Depending on the scoring system, you can copy/paste the article into a new position according to what your system dictates. Make sure it is the EXACT same statement (e.g., spelling, capitalization, punctuation) inside of the quotation marks. Otherwise, it won't work. 
    #Or, instead of re-arranging articles, if it makes sense, change the scores in lines 12 and 14 to reflect the new parameters. Right now, what this means is if a score is equal to or less than -2, you get the first post; if the score is greater than 2, you get that second post; for any other score (-1, 0, 1, 2) you get that third post.
    #Finally, if it does make sense, you can do some combination of the two options.
    if n < -1:
        article4 = "Transgender Peoples' Rights in the Military"
    elif n > 2:
        article4 = "Millenials: Ungrateful, Lazy, Tanking Our Economy"
    else:
        article4 = "These 10 Tips Will Get You The Job, Number 7 Will SHOCK You"
    return article4
