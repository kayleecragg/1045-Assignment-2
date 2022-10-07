from __future__ import annotations
from basic_AI import BasicAIPlayer
from cards import Card, Rank, Suit
import time


#from player import print_card


class Round:
  round_num = 1
  trick = []

  def __init__(self, players) -> None:
    self.trick_winner = None
    self.starting_player = None
    check = 0 
    r = True
    broken_hearts = False
   
    while r == True:
      Round.trick = []
      if self.trick_winner:
        self.starting_player = self.trick_winner

      else:
        #check which player has 2 of clubs to start
        lowest = None
        for i, player in enumerate(players):
            player.hand.sort()
            if lowest is None:
                lowest = player.hand[0]
                self.starting_player = i
            elif lowest > player.hand[0]:
                lowest = player.hand[0]
                self.starting_player = i
  
        #print("===",players[self.starting_player],"Starts the Round", Round.round_num,"===\n")
      
      #create order of play
      l1 = players[self.starting_player:len(players)]
      l2 = players[0:self.starting_player]
      order_of_play = l1+l2
  
      for i in range(len(players)):
        player = order_of_play[i]
        # print("Jacobs eyes only",len(player.hand))
        play = player.play_card(trick= Round.trick, broken_hearts = broken_hearts)
        Round.trick.append(play)

        time.sleep(0.5)
        print(player,"plays")
        print(play)
        time.sleep(0.5)
       
        if play.suit == Suit.Hearts and broken_hearts != True:
          print("Hearts have been broken!")
          broken_hearts = True
      
      #print(f"{player} playes {Round.trick}")
      suit_of_trick = Round.trick[0].suit
  
      #calculate who wins trick
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
          
      print(f"{Round.trick_winner} takes the trick. Points received {points}")
  
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
    print("========= End of round 1 =========")
    for player in players:
        player.total_score += player.round_score
        print(f"{player}'s round score: {player.round_score}")
        #print(f"{player}'s total score: {player.total_score}")
        player.round_score = 0
    print("")

    for player in players:
        player.total_score += player.round_score
        print(f"{player}'s total score: {player.total_score}")
        player.round_score = 0

    Round.round_num += 1


if __name__ == '__main__':
    import random
    deck = []
    for suit in Suit:
        for rank in Rank:
            if rank != Rank.Two:
                deck.append(Card(rank, suit))

    random.shuffle(deck)
    #print(deck)

    players = []
    for i in range(4):
        players.append(BasicAIPlayer("Player {0}".format(i + 1)))

    for i in range(len(deck)):
        p = i % 4
        players[p].hand.append(deck[i])

    r = Round(players)
      

    

    

      
      
    
 

    
    

    
          
        
    
    