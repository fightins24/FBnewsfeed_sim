#Go to line 17 for instructions! And, don't change lines 13, 14, or 15.
#I should note that after you run cell 7, the results might not make sense any more, so don't worry about that.

{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}


def finalposts(n):
    #don't change these! Leave lines 13/14/15 alone.
    article6 = "Friend's Post About Life Event/Selfie/Pyramid Scheme Proposition"
    FBpage1 = "Friend's Post About Life Event/Selfie/Pyramid Scheme Proposition"
    video2 = "Friend's Post About Life Event/Selfie/Pyramid Scheme Proposition"

    #Depending on the scoring system, you can copy/paste the articles in lines 22/23/24, 26/27/28, and 30/31/32 into a new position according to what your system dictates. Make sure it is the EXACT same statement (e.g., spelling, capitalization, punctuation) inside of the quotation marks. Otherwise, it won't work. 
    #Or, instead of re-arranging articles, if it makes sense, change the scores in lines 12 and 14 to reflect the new parameters. Right now, what this means is if a score is equal to or less than -3, you get the first post; if the score is greater than 4, you get that second post; for any other score (-2, -1, 0, 1, 2, 3) you get that third post.
    #Finally, if it does make sense, you can do some combination of the two options.
    if n < -2:
        article5 = "Pittsburgh is a Nationally Ranked Foodie Destination. Why are Residents Experiencing Food Insecurity?"
        article6 = "Are the Lizard People REAL Liberals? The Answer May Surprise You"
        video2 = "Schools are More Segregated Now Than They Were in the 1960s"
    elif n > 4:
        article5 = "Your Bridges: Are They Stable?"
        article6 = "Globalists Illuminati Deep State Lizard People: Watch this Video of Arrows Pointing at Things"
        video2 = "Terrorism in Europe: Why the US Needs More Vetting of Immigrants"
    else:
        article5 = "Your Bridges: Are They Stable?"
        article6 = "Puppies!!!!! Can They be Trusted? Are they Lizard People?!"
        FBpage1 = "Africa Water Scarcity Initiative: ACT NOW"
    
    print("Facebook likes to keep you engaged (see: ad $). These are the four posts you see based on your history:")
    print("1")
    print(article5)
    print("2")
    print(article6)
    print("3")
    print(FBpage1)
    print("4")
    print(video2)   
    
    share_post = int(input("----Of the four posts that are now in your feed, choose one to share. Type 1, 2, 3, or 4--the number corresponds with position "))
    if share_post == 1 or share_post == 2 or share_post == 3 or share_post == 4:
        print("You chose to share! Sharing is caring. Don't be shy, add your own text, too! Rhetorical velocity!")
    else:
        print("That is not a valid response, please enter a valid response")

    if share_post == 1:
        print("----What you are posting:")
        input("Text above shared post: ")
        print("article post: " + article5)
    
    if share_post == 2:
        print("----What you are posting:")
        input("Text above shared post: ")
        print("article post: " + article6)
   
    if share_post == 3:
        print("----What you are posting:")
        input("Text above shared post: ")
        if FBpage1 == "Africa Water Scarcity Initiative: ACT NOW":
            print("Facebook page: Africa Water Scarcity Initiative: ACT NOW")
        else:
            print("Friend's post about w/e: " + FBpage1)
    
    if share_post == 4:
        print("----What you are posting:")
        input("Text above shared post: ")
        if FBpage1 == "Africa Water Scarcity Initiative: ACT NOW":
            print("Friend's post about w/e: Friend's Post About Life Event/Selfie/Pyramid Scheme Proposition")
        else:
            print("video post: " + video2)
    return share_post