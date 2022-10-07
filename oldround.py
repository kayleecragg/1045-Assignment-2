from __future__ import annotations
from cards import Card, Rank, Suit
import time
from player import print_card


class Round:
  round_num = 1
  trick = []
  trick_winner = 0
  starting_player = 0
  def __init__(self, players) -> None:
    check = 0 
    r = True
    broken_hearts = False
    while r == True:
      Round.trick = []
      Round.starting_player = "null"
      #check which player has 2 of clubs to start
      two_of_clubs = Card(Rank.Two, Suit.Clubs)
      for i in range(len(players)):
        cards = players[i].hand
        for j in range(len(cards)):
          if cards[j] == two_of_clubs:
            Round.starting_player = i
  
      if Round.starting_player != "null":
        pass
      else:
        for i in range(len(players)):
          if players[i] == Round.trick_winner:
            Round.starting_player = i

      if check == 0:
        print("===",players[Round.starting_player],"Starts the Round", Round.round_num,"===\n")

      
      #create order of play
      l1 = players[Round.starting_player:len(players)]
      l2 = players[0:Round.starting_player]
      order_of_play = l1+l2
  
      for i in range(len(players)):
        player = order_of_play[i]
        # print("Jacobs eyes only",len(player.hand))
        play = player.play_card(trick= Round.trick, broken_hearts = broken_hearts)
        Round.trick.append(play)
        time.sleep(0.5)
        print(player,"plays: ")
        print(play)
        time.sleep(0.5)
        if play.suit == Suit.Hearts and broken_hearts != True:
          print("Hearts have been broken!")
          broken_hearts = True
      
      print("")
      print_card(Round.trick,False)
      suit_of_trick = Round.trick[0].suit
  
      #calculate who wins trick
      # print(order_of_play)
      winning_card = Round.trick[0]
      current_winner = order_of_play[0]
      for i in range(1,len(Round.trick)):
        if Round.trick[i].suit == suit_of_trick:
          if Round.trick[i].rank > winning_card.rank:
            winning_card = Round.trick[i]
            current_winner = order_of_play[i]
        
      Round.trick_winner = current_winner
      
  
  
      #Calculate points
      points = 0
      for i in range(0,len(Round.trick)):
        if Round.trick[i].suit == Suit.Hearts:
          points += 1
        if Round.trick[i] == Card(Rank.Queen, Suit.Spades):
          points += 13
          
      print("")
      print(f"{Round.trick_winner} takes the trick. Points received: {points} points")
      print("")
  
      #give points
      Round.trick_winner.round_score += points

      check += 1 
    
      if len(players[0].hand) == 0:
        r = False

    #shoot the moon
    moon = 0
    p = 0
    for i in range(len(players)):
      player = players[i]
      if player.round_score == 26:
        print(player, " has shot the moon! Everyone else receives 26 points\n")
        moon += 1
        p = i
    if moon > 0:
      for i in range(len(players)):
        player = players[i]
        player.round_score = 26
      players[p].round_score = 0
        
      
    
    # print end of round stats to see player objects updated
    print("====== End of Round Stats ======")
    for i in range(len(players)):
        player = players[i] 
        player.total_score += player.round_score
        print(f"{player}'s Round Score: {player.round_score}")
        player.round_score = 0
        print("")

    for i in range(len(players)):
        player = players[i] 
        player.total_score += player.round_score
        print(f"{player}'s Total Score: {player.total_score}")
        player.round_score = 0
        print("")

    Round.round_num += 1
    print("")