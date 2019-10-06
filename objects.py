class Cards:
    def __init__(self, value=None, suit=None):
        self.value = value
        self.suit = suit
    def __str__(self):
        return '{} {}'.format(self.value, self.suit)
class Deck:
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

    def __repr__(self):
        return 'В колоде {} карт.'.format(len(self.deck))

class Player:
    def __init__(self):
        self.cards = []
        self.score = int()
    def add_cards(self, card):
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

    def __repr__(self):
        return 'Ваш счет: {}\nВаша карта: {}'.format(self.score, self.cards[-1])
class Dealer(Player, Deck):
    def more(self):
        return self.deck.pop()


