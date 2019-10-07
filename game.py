import objects
from random import shuffle


def check_score(player_score, dealer_score, end=False):
    '''
    Функция проверяет количество очков у игрока и дилера.
    :param player_score: количество очков у игрока.
    :param dealer_score: количество очков у дилера.
    :param end: параметр, отвечающий за конец игры. Если True - игра закончена.
    :return: ход или итог игры.
    '''
    if (player_score > dealer_score and end is True) \
            or dealer_score > 21 or player_score == 21:
        return 'Ты выиграл.'
    elif player_score > 21 or player_score < dealer_score and end is True:
        return 'Ты проиграл.'
    else:
        return 'Идёт игра'


deck = objects.Deck()  # Колода
player = objects.Player()   # Игрок
dealer = objects.Dealer()   # Дилер
action = ''     # Действие игрока

shuffle(deck.deck)  # Перемешиваем колоду
# Ход игры
game_progress = 'Игра началась, колода помешана. В игре 2 игрока, Dealer и Player'
print(game_progress)
game_progress = 'Идёт игра'

# Цикл взаимодействия с пользователем в соответствии с правилами игры.
while game_progress == 'Идёт игра':
    print('1 - взять еще\n2 - закончить')
    action = input('Ваше действие: ')
    if action == '1':
        player.add_cards(dealer.more())
        dealer.add_cards(dealer.more())
        print(player)
        game_progress = check_score(player.score, dealer.score)
    elif action == '2':
        game_progress = check_score(player.score, dealer.score, end=True)
    print(game_progress)
print('Ваш счет: {}\nСчет dealer: {}'.format(player.score, dealer.score))
