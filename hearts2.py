from __future__ import annotations
import random
from cards import Card, Rank, Suit
from basic_ai import BasicAIPlayer
from round import Round



class Hearts:
  def __init__(self):
    #check if valid
    while True:
        try :
            target = int(input("Please enter a target score to end the game: "))
            if target > 0:
                break
        except ValueError:
            print("Enter a valid number")
      
    while True:
        try:
            num = int(input("Please enter the number of players (3-5): "))
            if num >=3 and num <= 5:
                break
        except ValueError:
            print("Please enter a valid number")
            
    #print("======= ♥ Welcome to Hearts ♥ =======\n")
    #create players 
    players = [BasicAIPlayer("P1"), BasicAIPlayer("Player 2"), BasicAIPlayer("Player 3"), BasicAIPlayer("Player 4"),BasicAIPlayer("Player 5")]
    players = players[0:num]

    #loop begins
    game = True
    while game == True:
      #create deck
      deck = []
      for i in Rank:
        for j in Suit:
          deck.append(Card(i,j))
  
      if num == 3:
        deck.remove(Card(Rank.Two,Suit.Diamonds))
      elif num == 5:
        deck.remove(Card(Rank.Two,Suit.Diamonds))
        deck.remove(Card(Rank.Two,Suit.Spades))
      cpp = int(len(deck)/num)
      
      #ASnounce
      print("========== Starting Round",Round.round_num," ==========")
      
      #assign hands
      for i in range(num):
        for j in range(cpp):
          c = random.choice(deck)
          deck.remove(c)
          
          players[i].hand.append(c)
  
      #check for forbidden hand
      for i in range(num):
        h_count = 0
        qs_count = 0
        error = 0 
        for j in range(cpp):
          if players[i].hand[j].suit == Suit.Hearts:
            h_count += 1
          if players[i].hand[j] == Card(Rank.Queen,Suit.Spades):
            qs_count += 1
          if (h_count + qs_count) == cpp:
            error = 1
            
          
        
      #if hand is forbidden redraw untill it isnt
      while error == 1:
        #reassign
        error = 0
        for i in range(num):
          for j in range(cpp):
            c = random.choice(deck)
            deck.remove(c)
            players[i].hand.append(c)

        #recheck
        for i in range(num):
          h_count = 0
          qs_count = 0
          for j in range(cpp):
            if players[i].hand[j].suit == Suit.Hearts:
              h_count += 0
            if players[i].hand[j] == Card(Rank.Queen,Suit.Spades):
              qs_count += 1
            if (h_count + qs_count) == cpp:
              error = 1
  
      #Pass Cards
      n = Round.round_num
      #human pass
      player = players[0]
      reciever = players[(n +i+1) % len(players)]
      card_list = player.pass_cards()
      reciever.hand.extend(card_list)
      print("Cards have been passed to", reciever)
      print("")
      #robot pass
      for i in range(1,len(players)):
        player = players[i]
        reciever = players[(n + i) % len(players)]
        card_list = player.pass_cards()
        for j in range(len(card_list)):
          reciever.hand.append(card_list[j])
          
        
      #excecute round
      Round(players)
      
      #test for winner
      lowest = target
      for i in range(len(players)):
        player = players[i]
        if player.total_score >= target:
          for j in range(len(players)):
            player = players[j]
            if player.total_score < lowest:
              lowest  = player.total_score
              winner = player
          game = False
          print("=======",winner,"wins with a score of",lowest,"=======")
          break



if __name__ == '__main__':
    Hearts()