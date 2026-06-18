import gymnasium as gym

env = gym.make("PongNoFrameskip-v4", render_mode="rgb_array")

obs, info = env.reset()

print("obs shape:", obs.shape)
print("action space:", env.action_space.n)

action = env.action_space.sample()
obs, reward, terminated, truncated, info = env.step(action)

print(reward)
env.close()