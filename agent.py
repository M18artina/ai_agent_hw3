import random

class QLearningAgent:
    def __init__(self, grid_size, num_actions, env, learning_rate=0.1, discount=0.9, epsilon=0.1):
        self.q_table = {}
        self.grid_size = grid_size
        self.num_actions = num_actions
        self.env = env
        self.lr = learning_rate
        self.gamma = discount
        self.epsilon = epsilon
        

    def get_state_key(self, state):
        return str((state, self.env.goal))  

    def get_q_values(self, state):
        key = self.get_state_key(state)
        if key not in self.q_table:
            self.q_table[key] = [0.0 for _ in range(self.num_actions)]
        return self.q_table[key]

    def choose_action(self, state):
        q_values = self.get_q_values(state)
        if random.random() < self.epsilon:
            return random.randint(0, self.num_actions - 1)
        else:
            return q_values.index(max(q_values))
    
    def update(self, state, action, reward, next_state, done):
        key = self.get_state_key(state)
        next_key = self.get_state_key(next_state)

        if key not in self.q_table:
            self.q_table[key] = [0.0 for _ in range(self.num_actions)]
        if next_key not in self.q_table:
            self.q_table[next_key] = [0.0 for _ in range(self.num_actions)]

        q_current = self.q_table[key][action]
        q_next_max = 0 if done else max(self.q_table[next_key])

        target = reward + self.gamma * q_next_max
        self.q_table[key][action] += self.lr * (target - q_current)
        
    



