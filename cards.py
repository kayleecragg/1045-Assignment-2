from __future__ import annotations # for type hints of a class in itself
from enum import Enum

class Rank(Enum):
	Two = 2
	Three = 3
	Four = 4
	Five = 5
	Six = 6
	Seven = 7
	Eight = 8
	Nine = 9
	Ten =10
	Jack = 11
	Queen = 12
	King = 13
	Ace = 14
	
	def __lt__(self, other: Rank) -> bool:
		return self.value < other.value
			
	
class Suit(Enum):
	Clubs = 1
	Diamonds = 2
	Spades = 3
	Hearts = 4
	
	def __lt__(self, other: Suit) -> bool:
		return self.value < other.value
				

class Card:

	def __init__(self, rank: Rank, suit: Suit) -> None:
		self.rank = rank
		self.suit = suit
		

	def __repr__(self) -> str:
		return self.__str__()
		
	def __str__(self) -> str:
		bank = {"Clubs": "♣","Hearts": "♥","Diamonds": "♦","Spades": "♠"}
		if self.rank.value <= 10:
			s1 = "┌─────┐\n"
			s2 = f"│{self.rank.value}".ljust(6," ")
			sin = "│\n"
			s3 = f"│  {bank[self.suit.name]}  │\n"
			sout = "│"
			s4 = f"{self.rank.value}│\n".rjust(7," ")
			s5 = "└─────┘"
			s = s1+s2+sin+s3+sout+s4+s5
		else:
			s1 = "┌─────┐\n"
			s2 = f"│{self.rank.name[0]}".ljust(6," ")
			sin = "│\n"
			s3 = f"│  {bank[self.suit.name]}  │\n"
			sout = "│"
			s4 = f"{self.rank.name[0]}│\n".rjust(7," ")
			s5 = "└─────┘"
			s = s1+s2+sin+s3+sout+s4+s5
			
		return s
		

	def __eq__(self, other: Card) -> bool:
		if (self.suit == other.suit) and (self.rank == other.rank):
			return True
		else:
			return False

	def __lt__(self, other: Card) -> bool:
		if (self.suit.value < other.suit.value):
			return True
		if (self.suit.value == other.suit.value):
			if (self.rank.value < other.rank.value):
				return True
			else:
				return False
		else:
			return False


# ♠
# ♥
# ♦
# ♣