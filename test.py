import random
from pprint import pprint
class Card(object):
    def __init__(self,suit,rank):
        self.suit = suit[0]
        self.char = suit[1].decode()
        self.rank = rank
        if self.rank.isnumeric():
            self.value = int(self.rank )
        elif self.rank == 'J':
            self.value=11
        elif self.rank == 'Q':
            self.value=12
        elif self.rank == 'K':
            self.value=13
        else:
            self.value=14
    
    def __repr__(self):
        return self.rank+' '+self.char
# class Deck():
#     def __init__(self):
#         self._cards = [Card(suit,rank) for rank in [str(i) for i in range(2,11)]+['J','Q','K','A'] for suit in [('Spades',b"\xE2\x99\xA0"),('Clubs',b"\xE2\x99\xA3"),('Hearts',b"\xE2\x99\xA5"),('Diamond',b"\xE2\x99\xA6")] ]

#     def shuffle(self):
#         random.shuffle(self._cards)

#     def draw(self):
#         return self._cards.pop(0)

#     def deal(self,num,pep):
#         case = dict()
#         for i in range(num):
#             for j in range(pep):
#                 if 'pep'+chr(97+j) not in case:
#                     case.setdefault('pep'+chr(97+j),[self.draw()])
#                 else:
#                     case['pep'+chr(97+j)].append(self.draw())        
#         return case
    
#     def __repr__(self):
#         return str(self._cards)



# new_Deck = Deck()
# new_Deck.shuffle()
# print(new_Deck)
# hand = new_Deck.deal(9,3)['pepa']

# input_hand = ['cK','eJ','e9','p8','c6','b5','b3','p2','e2']
# input_hand = ['bK','p6','e3','eK','p10','b2','eA','p4','e8']
# input_hand = ['bJ','bQ','b7','c10','eK','p7','c8','eQ','eA']
# input_hand = ['cJ','bA','cQ','b5','c4','b2','pQ','b6','c2']
# input_hand = ['e4','p4','b5','eQ','b10','cK','bJ','c10','c9']
input_hand = ['pQ','cQ','eQ','p2','p3','p6','b7','e7','b2']
hand= []
for item in input_hand:
    if item[0] == 'b':
        suit = ('Spades',b"\xE2\x99\xA0")
    if item[0] == 'c':
        suit = ('Clubs',b"\xE2\x99\xA3")
    if item[0] == 'p':
        suit = ('Hearts',b"\xE2\x99\xA5")
    if item[0] == 'e':
        suit =('Diamond',b"\xE2\x99\xA6")
    hand.append(Card(suit,item[1:]))

# supposed_hand = input_hand = ['bK','p6','e3','eK','p10','b2','eA','p4','e8']
# supposed_hand = input_hand = ['eA','b2','e3','p10','p4','p6','eK','bK','e8']
# supposed_hand = input_hand = ['bK','eK','e8','p6','p10','p4','e3','b2','eA']

supposed_final_hand= []
for item in input_hand:
    if item[0] == 'b':
        suit = ('Spades',b"\xE2\x99\xA0")
    if item[0] == 'c':
        suit = ('Clubs',b"\xE2\x99\xA3")
    if item[0] == 'p':
        suit = ('Hearts',b"\xE2\x99\xA5")
    if item[0] == 'e':
        suit =('Diamond',b"\xE2\x99\xA6")
    supposed_final_hand.append(Card(suit,item[1:]))