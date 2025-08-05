import random

class GridWorld:
    def __init__(self, size=5):
        self.size = size  # velikost mřížky (5x5)
        self.start = (0, 0)  # počáteční pozice agenta
        self.goal = (size - 1, size - 1)  # cílová pozice (pravý dolní roh)
        self.agent_pos = self.start  # aktuální pozice agenta

    def reset(self):
        self.agent_pos = self.start
        self.random_goal()
        return self.agent_pos

    def step(self, action):
        x, y = self.agent_pos

        # ↑ 0, ↓ 1, ← 2, → 3
        if action == 0 and y > 0:
            y -= 1
        elif action == 1 and y < self.size - 1:
            y += 1
        elif action == 2 and x > 0:
            x -= 1
        elif action == 3 and x < self.size - 1:
            x += 1

        self.agent_pos = (x, y)

        reward = -0.01
        done = False

        if self.agent_pos == self.goal:
            reward = 1
            done = True

        return self.agent_pos, reward, done

    def render(self):
        for y in range(self.size):
            row = ''
            for x in range(self.size):
                if (x, y) == self.agent_pos:
                    row += 'A '
                elif (x, y) == self.goal:
                    row += 'G '
                else:
                    row += '. '
            print(row)
        print()
    
    def random_goal(self):
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if (x, y) != self.start:
                self.goal = (x, y)
                break
