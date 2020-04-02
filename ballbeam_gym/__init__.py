from gym.envs.registration import register

__version__ = '0.0.5'

register(
    id='BallBeamBalance-v0',
    entry_point='ballbeam_gym.envs:BallBeamBalanceEnv',
)

register(
    id='VisualBallBeamBalance-v0',
    entry_point='ballbeam_gym.envs:VisualBallBeamBalanceEnv',
)


