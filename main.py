from cards import Card, Rank, Suit
from basic_AI import BasicAIPlayer
from oldround import Round
from oldheart import Hearts
from player import HumanPlayer
from player import Player

# #TEST CODE
# players = [BasicAIPlayer("Player 1"), BasicAIPlayer("Player 2"), BasicAIPlayer("Player 3"), BasicAIPlayer("Player 4"),BasicAIPlayer("Player 5")]
# players = players[0:4]
# players[0].hand = [Card(Rank.Four, Suit.Diamonds), Card(Rank.King, Suit.Clubs), Card(Rank.Nine, Suit.Clubs), Card(Rank.Ace, Suit.Hearts)]
# players[1].hand = [Card(Rank.Two, Suit.Clubs), Card(Rank.Four, Suit.Spades), Card(Rank.Nine, Suit.Spades), Card(Rank.Six, Suit.Diamonds)]
# players[2].hand = [Card(Rank.Seven, Suit.Diamonds), Card(Rank.Ace, Suit.Spades), Card(Rank.Jack, Suit.Diamonds), Card(Rank.Queen, Suit.Spades)]
# players[3].hand = [Card(Rank.Queen, Suit.Hearts), Card(Rank.Jack, Suit.Clubs), Card(Rank.Queen, Suit.Diamonds), Card(Rank.King, Suit.Hearts)]

# Round(players)

Hearts(10,5)

#test pass cards
# p1 = HumanPlayer()
# p2 = HumanPlayer()
# p1.hand = [Card(Rank.Four, Suit.Diamonds), Card(Rank.King, Suit.Clubs), Card(Rank.Nine, Suit.Clubs), Card(Rank.Ace, Suit.Hearts)]
# p1.pass_cards(p2)


# s = "┌─────┐\n│r    │\n│  s  │\n│    r│\n└─────┘"
# print(s)

# print(Card(Rank.Four, Suit.Diamonds).suit)
# # print(Card(Rank.King, Suit.Diamonds))


