import random
class Deck:
    def __init__(self):
        
        self.values = [str(i) for i in range(2,11)] + ["J","Q","K","A"]
        self.suits = ["D","H","C","S"]
        self.cards = []
        
        for suit in self.suits:
            for value in self.values:
                self.cards.append(value + suit)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self,n):
        dealed_cards = self.cards[-n:]
        self.cards = self.cards[:-n]
        return dealed_cards
    
    def sort_by_suit(self):
        custom_ordered_suits = ["H","D","C","S"]
        cards_by_suit = []
        for suit in custom_ordered_suits:
            for card in self.cards:
                if card[-1] == suit :
                    cards_by_suit.append(card)
        self.cards = cards_by_suit
    
    def contains(self,card):
        if card in self.cards:
            return True
        else:
            return False
    
    def copy(self):
        new_deck = Deck()
        new_deck.cards = self.get_cards()
        return new_deck
    
    def get_cards(self):
        return self.cards.copy()
    
    def __len__(self):
        return len(self.cards)