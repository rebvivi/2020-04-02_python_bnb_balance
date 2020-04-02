#! /usr/bin/env python3
import gym
import ballbeam_gym
import matplotlib.pyplot as plt

# pass env arguments as kwargs


kwargs = {'timestep': 0.01,
            'beam_length':1.08,
            'max_angle':20*3.14/180,
            'init_velocity': 0.0,
            'max_timesteps': 500,
            'action_mode':'continuous'}
# create env
env = gym.make('BallBeamBalance-v0', **kwargs)

# constants for PID calculation
Kp = (30/7)
Kd =(13/7)
angle=[]
# simulate 1000 steps
for i in range(300):   
    # control theta with a PID controller
    env.render()
    theta = Kp*(env.bb.x ) + Kd*(env.bb.v)
    obs, reward, done, info = env.step(theta)
    e,f,g=obs
    angle.append(g)
    if done:
        env.reset()


