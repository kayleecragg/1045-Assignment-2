from __future__ import annotations
from cards import Card, Rank, Suit
from player import Player

class BasicAIPlayer(Player):

	def __init__(self, name: str):
		super().__init__(name)
	
	def play_card(self, trick: list[Card], broken_hearts: list[Card]) -> Card:
		hand_val = []
		for i in range(len(self.hand)):
			c = self.hand[i]
			hand_val.append(c.rank.value)
		hand_val.sort()
		for i in range(len(hand_val)):
			for j in range(len(hand_val)):
				c = self.hand[j]
				if c.rank.value == hand_val[i]:
					check = self.check_valid_play(self.hand[j],trick, broken_hearts)
					if check[0] == True:
						c = self.hand[j]
						self.hand.remove(c)
						return c
		

	def pass_cards(self) -> Card:
		rev = (sorted(self.hand))
		card_list = rev[len(self.hand)-3:len(self.hand)]
		for i in range(3):
			self.hand.remove(card_list[i])
		return card_list

