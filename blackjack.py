# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:59:26 2021

@author: Charles
"""
import art
import random


def deal_card():
    """RETURNS RANDOM CARD FROM DECK"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """TAKES A LIST OF CARDS AND RETURNS CALCULATES SCORE FOR DEALT CARDS"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """COMPARES USER AND COMPUTER SCORE AND GETS WINNER"""
    if user_score == computer_score:
        return "Stand"
    elif computer_score == 0:
        return "Lose, Dealer has Blackjack"
    elif user_score == 0:
        return "Winner with Blackjack"
    elif user_score > 21:
        return "Lose, You went bust."
    elif computer_score > 21:
        return "Winner, Dealer went bust."
    elif user_score > computer_score:
        return "Player Wins"
    else:
        return "Dealer Wins"
def play_game():
    user_cards = []
    computer_cards = []
    isGameOver = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not isGameOver:
        print(art.logo)
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")    
         
        if user_score == 0 or computer_score == 0 or user_score >21:
            isGameOver = True
        else:
            user_should_deal = input("Type 'y' to take another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                isGameOver = True
                
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)             
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Type 'y' to play a game of Blackjack, type 'n' to leave: ").lower() == "y":
    play_game()
       