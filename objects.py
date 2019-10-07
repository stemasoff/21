"""
Модуль objects.py содержит в себе классы, которые будут
взаимодействовать в ходе игры.
"""

class Cards:
    """
    Класс карты имеет два параметра, значение и масть.
    """
    def __init__(self, value=None, suit=None):
        self.value = value
        self.suit = suit
    def __str__(self):
        return '{} {}'.format(self.value, self.suit)
class Deck:
    """
    Колода содержит в себе 36 объектов класса Карта.
    """
    value = [i for i in range(6, 11)]
    value.append('J')
    value.append('Q')
    value.append('K')
    value.append('A')
    suit = ['Heart', 'Diamond', 'club', 'spade']
    deck = []
    for i in value:
        for j in suit:
            deck.append(Cards(i, j))

    def __str__(self):
        return 'В колоде {} карт.'.format(len(self.deck))

class Player:
    """
    Класс player имеет 2 параметра, это карта, и его счет.
    Player может взять карту и посчитать, сколько у него очков.
    """
    def __init__(self):
        self.cards = []
        self.score = int()
    def add_cards(self, card):
        '''
        Функция принимает карту и считает, сколько очков у player.
        :param card: экземпляр класса Cards
        '''
        self.cards.append(card)
        if isinstance(self.cards[-1].value, int):
            self.score = self.score + self.cards[-1].value
        elif self.cards[-1].value == 'J':
            self.score = self.score + 2
        elif self.cards[-1].value == 'Q':
            self.score = self.score + 3
        elif self.cards[-1].value == 'K':
            self.score = self.score + 4
        else:
            self.score = self.score + 11

    def __str__(self):
        return 'Ваш счет: {}\nВаша карта: {}'.format(self.score, self.cards[-1])

class Dealer(Player, Deck):
    """
    Класс dealer наследует все свойства от класса player и deck.
    Dealer может снимать с колоды последнюю карту.
    """
    def more(self):
        return self.deck.pop()


