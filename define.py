import random

# data initialize
card = list(range(1,53))
suit = ['spade','heart','diamond','club']
cardName = { 1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 0: 'King' }

# reset player and com hand card
def game_start():
    print('welcome')
    player_card = []
    com_card = []
    
# draw a card from deck
def draw(listname):
    while True:
        num = random.randint(0,51)
        if card[num] != ' ':
            draw = card[num]
            card[num] = ' '
            break
    listname.append(draw)

# count the points of hand card
def count_points(listname):
    count = 0
    amount_ace = 0
    for i in listname:
        point = i%13
        if point == 0 or point == 11 or point == 12:
            point = 10
        if point == 1:
            point = 11
            amount_ace += 1
        count += point
    while count > 21:
        if amount_ace > 0:
            count -= 10
            amount_ace -= 1
        else:
            break
    return count

# display com's hand cards
def show_card_com_1():
    if (com_card[0]//13)-1 < 0:
        num = 0
    else:
        num = (com_card[0]//13)-1
    suits = suit[num]
    cardname = cardName[com_card[0]%13]
    print("Computer Shows :",cardname,"of",suits)
    
# display player's hand cards    
def show_card_player():
    print("Your Hand :")
    for card in player_card:
        if (player_card[0]//13)-1 < 0:
            num = 0
        else:
            num = (player_card[0]//13)-1
        suits = suit[num]
        cardname = cardName[card%13]
        print(cardname,"of",suits)
    print("Count :",count_points(player_card))
    
# display com's hand cards
def show_card_com():
    print("Computer Hand :")
    for card in com_card:
        if (com_card[0]//13)-1 < 0:
            num = 0
        else:
            num = (com_card[0]//13)-1
        suits = suit[num]
        cardname = cardName[card%13]
        print(cardname,"of",suits)
    print("Count :",count_points(com_card))
    
# check points if more than 21
def check_more_than_21(listname):
    if count_points(listname) > 21:
        return True

# show both player and com's hand cards
def end_print():
    print("--------------")
    show_card_player()
    show_card_com()
