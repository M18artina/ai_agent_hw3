from environment import GridWorld
from agent import QLearningAgent
import matplotlib.pyplot as plt
import numpy as np

# Inicializace prostředí a agenta
env = GridWorld(size=5)
agent = QLearningAgent(
    grid_size=5,
    num_actions=4,
    env=env,
    learning_rate=0.1,
    discount=0.9,
    epsilon=0.9 
)

# Tréninková smyčka
num_episodes = 500

# Pro sledování nejkratší cesty a nejlepších odměn
best_path = []
best_length = float('inf')
best_rewards = {}  

for episode in range(num_episodes):
    state = env.reset()
    total_reward = 0
    path = [state]
    current_goal = env.goal  

    for step in range(100):  
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)

        agent.update(state, action, reward, next_state, done)

        state = next_state
        path.append(state)
        total_reward += reward

        if done:
            break
    
    # Nejlepší odměna pro daný cíl
    goal_key = str(current_goal)
    if goal_key not in best_rewards or total_reward > best_rewards[goal_key]:
        best_rewards[goal_key] = total_reward

    # Nejkratší trajektorie
    if done and len(path) < best_length:
        best_length = len(path)
        best_path = path.copy()
    
    # Snížení náhodnosti
    agent.epsilon = max(0.01, agent.epsilon * 0.995)

    if (episode + 1) % 50 == 0:
        print(f"Epizoda {episode+1}: odměna = {round(total_reward, 2)}")


# Test po tréninku – bez náhodných akcí
print("\n Test po tréninku (epsilon = 0 - čisté využití naučených Q-hodnot):")
agent.epsilon = 0.0

state = env.reset()
env.render()

for step in range(20):
    action = agent.choose_action(state)
    state, reward, done = env.step(action)
    env.render()
    if done:
        print(f"Agent dosáhl cíle za {step+1} kroků!")
        break
else:
    print("Agent se do cíle nedostal.")


# Výpis nejlepší trajektorie
print(f"\n Nejkratší nalezená trajektorie ({len(best_path)-1} kroků):")
for i, pos in enumerate(best_path):
    print(f"  {i+1}. {pos}")


# Výpis nejlepších odměn pro jednotlivé cíle
print("\n Nejlepší dosažené odměny podle cílových pozic:")
for goal, reward in best_rewards.items():
    print(f"  Cíl {goal}: odměna = {round(reward, 2)}")


# Vizualizace heatmapy Q-hodnot
heatmap = np.zeros((env.size, env.size))

for key in agent.q_table:
    (x, y), _ = eval(key)  # klíč = (pozice, goal)
    max_q = max(agent.q_table[key])
    heatmap[x, y] = max_q

plt.figure(figsize=(6, 5))
plt.imshow(heatmap, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title("Heatmapa maximálních Q-hodnot (stavová jistota agenta)")
plt.xlabel("y")
plt.ylabel("x")
plt.xticks(np.arange(env.size))
plt.yticks(np.arange(env.size))
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
