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
        for i in self.cards:
            if isinstance(i.value, int):
                self.score = self.score + i.value
            elif i.value == 'J':
                self.score = self.score + 2
            elif i.value == 'Q':
                self.score = self.score + 3
            elif i.value == 'K':
                self.score = self.score + 4
            else:
                self.score = self.score + 11
            print('Итерации score: {}'.format(self.score))
    def __repr__(self):
        return 'Ваш счет: {}'.format(self.score)
class Dealer(Player, Deck):
    def more(self):
        return self.deck.pop()


