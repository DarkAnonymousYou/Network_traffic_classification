import gym
import numpy as np

# Create the CartPole environment
env = gym.make('CartPole-v1')

# Number of state features
state_size = env.observation_space.shape[0]

# Number of possible actions (left or right)
action_size = env.action_space.n

print(f"State size: {state_size}, Action size: {action_size}")

# Run a single episode
for episode in range(1):  # Change 1 to any number of episodes you want to test
    # Reset the environment at the start of an episode
    state = env.reset()
    
    # Convert the state to a NumPy array and reshape for compatibility
    state = np.array(state, dtype=np.float32).reshape(1, -1)
    
    print(f"Initial state (reshaped): {state}, Shape: {state.shape}")
    
    for t in range(500):  # Max timesteps
        env.render()  # Visualize the environment
        
        # Take a random action
        action = env.action_space.sample()
        
        # Perform the action and observe the result
        next_state, reward, done, _ = env.step(action)
        
        # Convert next_state to a NumPy array and reshape for compatibility
        next_state = np.array(next_state, dtype=np.float32).reshape(1, -1)
        
        print(f"Step: {t+1}, Action: {action}, Reward: {reward}, Done: {done}, Next state shape: {next_state.shape}")
        
        # Break the loop if the episode ends
        if done:
            print(f"Episode finished after {t+1} timesteps")
            break

env.close()
