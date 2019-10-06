import objects
from random import shuffle

def check_score(player_score, dealer_score, end = None):
    if (player_score > dealer_score and end != None) or dealer_score > 21 or player_score == 21:
        return 'Ты выиграл. Счет dealer {}'.format(dealer_score)
    elif end == None:
        return 'Игра продолжается'
    else:
        return 'Ты проиграл. Счет dealer {}'.format(dealer_score)

deck = objects.Deck()
player = objects.Player()
dealer = objects.Dealer()
action = ''


shuffle(deck.deck)

print('Игра началась, колода помешана. В игре 2 игрока, Dealer и Player')
i = 0
while action != '2':

    print('1 - взять еще\n2 - закончить')
    action = input('Ваше действие: ')
    if action == '1':
        player.add_cards(dealer.more())
        dealer.add_cards(dealer.more())
        print(player)
        print(dealer)
        print(player.cards[i])
        print(dealer.cards[i])
        print(check_score(player.score, dealer.score))
    elif action == '2':
        print(check_score(player.score, dealer.score, end = 1))
    i += 1