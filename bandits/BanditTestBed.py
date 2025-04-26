import numpy as np

class Bandit:
    def __init__(self, num_arms):
        self.num_arms = num_arms
        self.arms = np.random.normal(0, 1, self.num_arms)

    def use_arm(self, arm):
        if arm >= 0 and arm < self.num_arms:
            return np.random.normal(self.arms[arm], 1)
    
    def get_best_arm(self):
        max_idx, _ = max(enumerate(self.arms), key=lambda pair: pair[1])
        return max_idx

class BanditTestBed:
    def __init__(self, num_arms, solver):
        self.bandit = Bandit(num_arms)
        self.solver = solver
    
    def run(self, iterations):
        rewards = []
        arm_choices = []
        total_reward = 0
        for _ in range(iterations):
            reward, arm = self.solver.select_arm(self.bandit)
            rewards.append(reward)
            arm_choices.append(arm)
            total_reward += 0
        
        average_reward = total_reward / iterations
        best_arm = self.bandit.get_best_arm()
        
        return rewards, arm_choices, self.bandit.arms, best_arm, average_reward

