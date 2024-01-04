#!/usr/bin/env python
# coding: utf-8

# In[1]:


# User Input: Prompt the user to choose rock, paper, or scissors.
# Computer Selection: Generate a random choice (rock, paper, or scissors) for
# the computer.
# Game Logic: Determine the winner based on the user's choice and the
# computer's choice.
# Rock beats scissors, scissors beat paper, and paper beats rock.
# Display Result: Show the user's choice and the computer's choice.
# Display the result, whether the user wins, loses, or it's a tie.
# Score Tracking (Optional): Keep track of the user's and computer's scores for
# multiple rounds.
# Play Again: Ask the user if they want to play another round.
# User Interface: Design a user-friendly interface with clear instructions and
# feedback
import random

a=['rock','paper','scissor']
comp=random.choice(a)
user=input("choose ROCK  PAPER  SCISSOR")
if user==comp:
    print("its tie")
elif user=='rock':
    user1=0
    comp1=0
    if comp=='paper':
        comp1+=1
        print("comp wins",comp)
        print("user score => ",user1)
        print("computer score => ",comp1)
    elif comp=='scissor':
        user1+=1
        print("user wins")
        print("user score => ",user1)
        print("computer score => ",comp1)
elif user=='paper':
    if comp=='rock':
        user1+=1
        print("user wins")
        print("user score => ",user1)
        print("computer score => ",comp1)
    elif comp=='scissor':
        comp1+=1
        print("comp wins",comp)
        print("user score => ",user1)
        print("computer score => ",comp1)
elif user=='scissor':
    if comp=='rock':
        comp1+=1
        print("comp wins",comp)
        print("user score => ",user1)
        print("computer score => ",comp1)
    elif comp=='paper':
        user1+=1
        print("user wins")
        print("user score => ",user1)
        print("computer score => ",comp1)


# In[ ]:




