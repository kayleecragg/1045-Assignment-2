from __future__ import annotations
from cards import Card, Rank, Suit
import time


class Player:

	def __init__(self, name: str):
		self.name = name
		self.hand = []
		self.round_score = 0
		self.total_score = 0


	def __str__(self) -> str:
		return f"{self.name}"

	def __repr__(self) -> str:
		return self.__str__()

	def check_valid_play(self, card: Card, trick: list[Card], broken_hearts: bool) -> tuple(bool, str):
		if len(trick) == 0:
			bank = 0
			h = 0
			for i in range(len(self.hand)):
				c = self.hand[i]
				if c != Card(Rank.Two, Suit.Clubs):
					bank += 1
				if c.suit == Suit.Hearts:
					h += 1
			if bank != len(self.hand) and card != Card(Rank.Two, Suit.Clubs):
				return [False,"Must Play 2 of Clubs"]
			if broken_hearts == False and h != len(self.hand) and card.suit == Suit.Hearts:
				return [False,"Cannot Lead with a heart"]
			else:
				return [True,"Valid Play"]
		else:
			s = 0
			for i in range(len(self.hand)):
				c = self.hand[i]
				if c.suit != trick[0].suit:
          
					s += 1
			if card.suit != trick[0].suit and s != len(self.hand):
				return [False,"Must Follow Suit"]
			if s == len(self.hand) and trick[0] == Card(Rank.Two, Suit.Clubs):
				if card.suit == Suit.Hearts or card == Card(Rank.Queen, Suit.Spades):
					return [False,"Cannot Play hearts or Queen of Spades on first trick"]	
		return [True,"Valid Play"]


class HumanPlayer(Player):
  
  def __init__(self):
    name = input("Input Player Name: ")
    super().__init__(name)
    
  def play_card(self, trick: list[Card], broken_hearts: list[Card]) -> Card:
    print("\nCurrent Trick:")
    print_card(trick,False)
    time.sleep(1)
    print("Current Hand:")
    print_card(self.hand,True)
    time.sleep(1)
    hand = False
    while hand == False:
      c = False
      while c == False:
        try:
          choice = int(input("Select a valid card to play: "))
          if 0 <= choice and choice < len(self.hand):
            c = True
          else:
            print("Choice must be within hand range")
        except:
          print("Please enter a number")
          choice  = -1
        
      check = self.check_valid_play(self.hand[choice],trick, broken_hearts)
      card = self.hand[choice]
      if check[0] == True:
        print("")
        self.hand.remove(card)
        return card
        break
      else:
        print(check[1])

      

  def pass_cards(self, passing_to) -> Card:
    print_card(self.hand,True)
    while True:
      str = input("Select three cards to pass off (e.g. '0, 4, 5'): ")
      try:
        if len(str) == 5:
          if int(str[0]) < int(str[2]) < int(str[4]):
            if (str[1]) == (str[3]) == ",":
              c = 0
              for i in range(0,6,2):
                if 0 <= int(str[i]) and int(str[i]) < len(self.hand):
                  c += 1
              if c == 3:
                break
              else:
                print("Please make sure numbers are within range\n")
            else:
              print("Please make sure numbers are separated by commas\n")
          else:
            print("Please make sure number are in accending order\n")
        else: 
          print("Please only enter 3 numbers\n")
      except:
        print("Please enter position in the form num1,num2,num3")
    list = [self.hand[int(str[0])],self.hand[int(str[2])],self.hand[int(str[4])]]
    for i in range(3):
      self.hand.remove(list[i])
      passing_to.hand.append(list[i])

def print_card(table,num):
  if table == []:
    print(table,"\n")
  else:
    for i in range(5):
      for j in range(len(table)):
        t = str(table[j])
        print(t[0+8*i:7+8*i],end = " ")
      print()
    if num == True:
      for i in range(len(table)):
  	      print(f"   {i}   ",end = " ")
      print("\n")
    
      
      
      
    
  
      
  

  