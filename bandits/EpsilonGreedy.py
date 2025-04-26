from BanditTestBed import Bandit
import random

class EpsilonGreedy:
    def __init__(self, num_arms, epsilon):
        self.num_arms = num_arms
        self.epsilon = epsilon
        self.rewards = [0]*self.num_arms
        self.num_tries = [0]*self.num_arms

    def choose_arm(self):
        r = random.random()
        if r < self.epsilon:
            arm = random.randint(0, self.num_arms-1)
        else:
            greedy_val = max(self.rewards)
            greedy_choices = [key for (key, val) in enumerate(self.rewards) if val == greedy_val]
            arm = greedy_choices[random.randint(0, len(greedy_choices) - 1)]
        return arm

    def select_arm(self, bandit):
        arm = self.choose_arm()
        
        reward = bandit.use_arm(arm)
        tries = self.num_tries[arm]
        if tries != 0:
            self.rewards[arm] += 1/tries * (reward - self.rewards[arm])
        else:
            self.rewards[arm] = reward
        self.num_tries[arm] += 1

        return reward, arm