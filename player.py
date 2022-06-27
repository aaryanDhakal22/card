from test import hand,supposed_final_hand,Card
from pprint import pprint
print(supposed_final_hand)
from itertools import permutations
perm = permutations(hand)
a = list(perm)
b = list()

def rating(hand):
    # print(hand)
    card1,card2,card3 = sorted(hand,key = lambda x : x.value)
    # print(card1.value)
    # print(card2.value)
    # print(card3.value)
    
    if card1.rank == card2.rank == card3.rank:
        # print('Trial Detected')
        rated = 6 + (card1.value/100)

    elif (card3.value == 14 and card1.value == 2 and card2.value ==3) or (card1.value + 1 == card2.value and card2.value + 1 == card3.value):
        # print("hi")
        rated = 4 + (card3.value/100)
        
        # print('Run Detected')
        if card1.suit == card2.suit == card3.suit:
            rated +=1.0        
            # print('Dab Detected')

        
    elif card1.suit == card2.suit == card3.suit:
        # print('Flash Detected')

        rated = 3 + (card3.value/100)

    elif len(set(hand)) != len(hand):
        # print('Jut Detected')

        if card1.value == card2.value :
            rated = 2+ (card1.value/100)
        if card2.value == card3.value :
            rated = 2+ (card2.value/100)
    
    else:
        # print('Badi Detected')

        rated = 1+(card3.value/100)

    return rated


    
     

# i = supposed_final_hand
for i in a :
    first = i[:3]
    second = i[3:6]
    third = i[6:9]
    # print(rating(first))
    # print(rating(second))
    # print(rating(third))
    # rates = (rating(first)*10)+(rating(second)*100)+(rating(third)*100)
    rates = (rating(first)*100) + (rating(second)*10) + rating(third)
    b.append((i,rates))
    # print(i,rates)

pprint(sorted(b, key = lambda x : x[1], reverse=True)[0])

# pprint(b)
