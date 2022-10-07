from __future__ import annotations
from cards import Card, Rank, Suit


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
			hearts = 0
			for i in range(len(self.hand)):
				c = self.hand[i]
				if c != Card(Rank.Two, Suit.Clubs):
					bank += 1
				if c.Suit == hearts:
					hearts += 1
			if bank != len(self.hand) and card != Card(Rank.Two, Suit.Clubs):
				return [False,"Must Play 2 of Clubs"]
			if broken_hearts == False and hearts != len(self.hand) and card.Suit == hearts:
				return [False,"Cannot Lead with a heart"]
			else:
				return [True,"Valid Play"]
		else:
			suit = 0
			for i in range(len(self.hand)):
				c = self.hand[i]
				if c.Suit != trick[0].Suit:
          
					suit += 1
			if card.Suit != trick[0].Suit and suit != len(self.hand):
				return [False,"Must Follow Suit"]
			if suit == len(self.hand) and trick[0] == Card(Rank.Two, Suit.Clubs):
				if card.Suit == Suit.Hearts or card == Card(Rank.Queen, Suit.Spades):
					return [False,"Cannot Play hearts or Queen of Spades"]	
		return [True,"Valid Play"]


class HumanPlayer(Player):
  
  def __init__(self):
    name = input("Input Player Name: ")
    super().__init__(name)
    
  def play_card(self, trick: list[Card], broken_hearts: list[Card]) -> Card:
    print("Current Trick:",trick)
    print("Current Hand:", self.hand)
    hand  = False
    while hand == False:
      choice = input("What position card would you like to play from your hand (0 = position 1, 1 = position 2 etc): ")
      check = self.check_valid_play(self.hand[choice],trick, broken_hearts)
      if check[0] == True:
        hand == True
      else:
        print(check[1])
      

  def pass_cards(self, passing_to) -> Card:
    print("")
    print("Current Hand",self.hand,"\n")
    while True:
      print("Input the position of the cards you wish to pass to",passing_to,":")
      str = input("")
      try:
        if len(str) == 4:
          if int(str[0]) < int(str[2]) < int(str[4]):
            if (str[1]) == (str[3]) == ",":
              c = 0
              for i in range(0,6,2):
                if 0 <= int(str[i]) and int(str[i]) < len(self.hand):
                  c += 1
              if c == 3:
                break
              else:
                print("Please make sure numbers are within range")
            else:
              print("Please make sure numbers are separated by commas")
          else:
            print("Please make sure number are in accending order")
        else:
          print("Please only enter 3 numbers")
          
      except:
        print("Please enter position in the form num1,num2,num3")
    list = [self.hand[int(str[0])],self.hand[int(str[2])],self.hand[int(str[4])]]
    print("Passing",list,"to",passing_to)
    passing_to.hand.append(list)
      
  

  