import objects
from random import shuffle

def check_score(player_score, dealer_score, end = False):
    if (player_score > dealer_score and end == True) \
            or dealer_score > 21 or player_score == 21:
        return 'Ты выиграл.'
    elif end == False:
        return 'Игра продолжается'
    else:
        return 'Ты проиграл.'

deck = objects.Deck()
player = objects.Player()
dealer = objects.Dealer()
action = ''


shuffle(deck.deck)
game_progress = 'Игра началась, колода помешана. В игре 2 игрока, Dealer и Player'
print(game_progress)

while action != '2' or game_progress == 'Игра продолжается':
    print('1 - взять еще\n2 - закончить')
    action = input('Ваше действие: ')
    if action == '1':
        player.add_cards(dealer.more())
        dealer.add_cards(dealer.more())
        print(player)
        game_progress = check_score(player.score, dealer.score)
    elif action == '2':
        game_progress = check_score(player.score, dealer.score, end = True)
    print(game_progress)
print(game_progress)
print('Ваш счет: {}\nСчет dealer: {}'.format(player.score, dealer.score))