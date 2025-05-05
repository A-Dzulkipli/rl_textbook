import numpy as np
import random

class BlackJack:
    def __init__(self):
        self.cards = [4]*9
        self.cards.append(16)
        self.card_count = 52
        self.player_cards = []
        self.dealer_cards = []
        self.player_total = 0
        self.dealer_total = 0

    def select_card(self):
        card = random.randint(1, self.card_count)
        total = 0
        idx = 0
        while total < card:
            total += self.cards[idx]
            idx += 1
        self.cards[idx-1] -= 1
        self.card_count -= 1
        return idx
    
    def deal(self):
        cards = []
        for _ in range(3):
            cards.append(self.select_card())
        return cards
    
    def setup(self):
        self.cards = [4]*9
        self.cards.append(16)
        self.card_count = 52
        self.player_cards = []
        self.dealer_cards = []
        self.player_total = 0
        self.dealer_total = 0

        cards = self.deal()
        self.player_cards.append(cards[0])
        self.player_cards.append(cards[1])
        self.dealer_cards.append(cards[2])
        self.player_total = np.sum(self.player_cards)
        self.dealer_total = np.sum(self.dealer_cards)

        return [[self.player_cards, self.player_total, self.dealer_cards, self.dealer_total], 0, False]
    
    def get_move(self):
        while True:
            move = input("Hit or Stay\n")
            if move == "Hit" or move == "Stay":
                return move
            

    def make_move(self, move):
        if move == "Hit":
            self.player_cards.append(self.select_card())
            self.player_total = np.sum(self.player_cards)
            if self.player_total > 21:
                reward = -1
                game_over = True
            else:
                reward = 0
                game_over = False
            
        elif move == "Stay":
            while self.dealer_total < 16:
                self.dealer_cards.append(self.select_card())
                self.dealer_total = np.sum(self.dealer_cards)
            
            if self.dealer_total > 21 or self.player_total > self.dealer_total:
                reward = 1
                game_over = True
            elif self.player_total == self.dealer_total:
                reward = 0
                game_over = True
            else:
                reward = -1
                game_over = True
        
        return [[self.player_cards, self.player_total, self.dealer_cards, self.dealer_total], reward, game_over]


    def run_game(self):
        self.setup()
        print(f"Player cards: {self.player_cards}, Total: {self.player_total}")
        print(f"Dealer cards: {self.dealer_cards}, Total: {self.dealer_total}")

        while self.player_total < 21 and self.get_move() == "Hit":
            self.make_move("Hit")
            print(f"Player cards: {self.player_cards}, Total: {self.player_total}")

        if self.player_total <= 21:
            print(f"Player cards: {self.player_cards}, Total: {self.player_total}")
            output = self.make_move("Stay")
            print(f"Dealer cards: {self.dealer_cards}, Total: {self.dealer_total}")
            if output[1] == 1:
                print("Win")
            elif output[1] == 0:
                print("Push")
            elif output[1] == -1:
                print("Lose")
        else:
            print("Bust")
        
        
    


if __name__ == "__main__":
    test_blackjack = BlackJack()
    test_blackjack.run_game()