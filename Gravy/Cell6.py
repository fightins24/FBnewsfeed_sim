{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}


def finalposts(n):
    article6 = "Friend's Post About Life Event/Selfie/Pyramid Scheme Proposition"
    FBpage1 = "Friend's Post About Life Event/Selfie/Pyramid Scheme Proposition"
    video2 = "Friend's Post About Life Event/Selfie/Pyramid Scheme Proposition"

    if n <= -3:
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