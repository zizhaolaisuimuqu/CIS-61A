from Q1 import Card
class ProfessorCard(Card):
    cardtype = 'Professor'

    def effect(self, other_card, player, opponent):
        """
        Adds the attack and defense of the opponent's card to
        all cards in the player's deck, then removes all cards
        in the opponent's deck that share an attack or defense
        stat with the opponent's card.
        >>> test_card = Card('card', 300, 300)
        >>> professor_test = ProfessorCard('Professor', 500, 500)
        >>> opponent_card = test_card.copy()
        >>> test_deck = Deck([test_card.copy() for _ in range(8)])
        >>> player1, player2 = Player(test_deck.copy(), 'p1'), Player(test_deck.copy(), 'p2')
        >>> professor_test.effect(opponent_card, player1, player2)
        3 cards were discarded from p2's deck!
        >>> [(card.attack, card.defense) for card in player1.deck.cards]
        [(600, 600), (600, 600), (600, 600)]
        >>> len(player2.deck.cards)
        0
        """
        orig_opponent_deck_length = len(opponent.deck.cards)
        copy = opponent.deck.cards[:]
        for card in player.deck.cards:
            card.attack += other_card.attack
            card.defense += other_card.defense
        for card in copy:
            if card.attack == other_card.attack or card.defense == other_card.defense:
                opponent.deck.cards.remove(card)
        discarded = orig_opponent_deck_length - len(opponent.deck.cards)
        if discarded:
            print('{} cards were discarded from {}\'s deck!'.format(discarded, opponent.name))
            return
