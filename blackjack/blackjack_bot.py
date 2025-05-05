import numpy as np
import pandas as pd
import pickle
import random

from blackjack import BlackJack

class SimpleBlackJackBot:
    def __init__(self, state=None):
        if state is None:
            self.state = {
                (player, dealer) : {
                    "Hit" : [0,0],
                    "Stay" : [0,0]
                }
                for player in range(2, 22)
                for dealer in range(1, 11)
            }
        else:
            with open(state, 'rb') as f:
                self.state = pickle.load(f)

    def choose_move(self, player_total, dealer_total):
        r = random.random()
        if r < 0.1:
            r = random.random()
            if r < 0.5:
                return "Hit"
            else:
                return "Stay"
        if self.state[(player_total, dealer_total)]["Hit"][0] > self.state[(player_total, dealer_total)]["Stay"][0]:
            return "Hit"
        else:
            return "Stay"
        
    def run_sim(self, blackjack):
        game_state = blackjack.setup()
        actions = []
        while not game_state[2]:
            player_total = game_state[0][1]
            dealer_total = game_state[0][3]
            move = self.choose_move(player_total, dealer_total)
            actions.append([player_total, dealer_total, move])
            game_state = blackjack.make_move(move)

        reward = game_state[1]

        for action in actions:
            if self.state[(action[0], action[1])][action[2]][1] != 0:
                n = self.state[(action[0], action[1])][action[2]][1]
            else:
                n = 1
            # print(f"for player_total {action[0]} and dealer_total {action[1]} the state before is {self.state[(action[0], action[1])][action[2]][0] }")
            self.state[(action[0], action[1])][action[2]][0] += 1/n * (reward - self.state[(action[0], action[1])][action[2]][0])
            self.state[(action[0], action[1])][action[2]][1] += 1
            # print(f"for player_total {action[0]} and dealer_total {action[1]} the state after is {self.state[(action[0], action[1])][action[2]][0] }")

    def train_model(self, iter):
        blackjack = BlackJack()
        for _ in range(iter):
            self.run_sim(blackjack)
        with open('simple_data.pkl', 'wb') as f:
            pickle.dump(self.state, f)


    def output_data(self):
        for key, val in self.state.items():
            print(f"{key} {val["Hit"]} {val["Stay"]}")

if __name__ == "__main__":
    try:
        test = SimpleBlackJackBot("simple_data.pkl")
    except:
        test = SimpleBlackJackBot()
    # test.train_model(1000000)
    test.output_data()
        