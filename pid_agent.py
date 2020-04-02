import gym
import ballbeam_gym

# pass env arguments as kwargs
'''
kwargs = {'timestep': 0.05, 
          'setpoint': 0,
          'beam_length': 1.0,
          'max_angle': 0.2,
          'init_velocity': 0.0}
'''
                 
kwargs = {'timestep': 0.05,
            'beam_length':1.0,
            'max_angle':0.2,
            'init_velocity': 0.0,
            'max_timesteps': 500,
            'action_mode':'continuous'}
# create env
env = gym.make('BallBeamBalance-v0', **kwargs)

# constants for PID calculation
Kp = 2.0
Kd = 1.0

# simulate 1000 steps
for i in range(1000):   
    # control theta with a PID controller
    env.render()
    theta = Kp*(env.bb.x ) + Kd*(env.bb.v)
    obs, reward, done, info = env.step(theta)

    if done:
        env.reset()
