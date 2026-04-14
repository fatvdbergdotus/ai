## Q-Learning

Q-learning is a reinforcement learning algorithm used in artificial intelligence to help an agent learn the best actions to take in an environment. It is a **model-free** method, meaning the agent does not need prior knowledge of the environment and instead learns through trial and error.

The main idea of Q-learning is the **Q-value (quality value)**, which represents how good a particular action is in a given state. The agent explores different actions, receives rewards or penalties, and updates its Q-values over time to improve its decisions.

### Q-Learning Update Rule

Q(s, a) = Q(s, a) + α [ r + γ max Q(s', a') − Q(s, a) ]

Where:
- **s** = current state  
- **a** = action taken  
- **r** = reward received  
- **s'** = next state  
- **α (alpha)** = learning rate  
- **γ (gamma)** = discount factor  

### Applications
- Game playing  
- Robotics  
- Navigation systems  
- Decision-making problems  

Q-learning is powerful because it can learn optimal strategies even when the environment is unknown or uncertain.

Python code: [Q-learning](/python/Q-Learning.ipynb)
