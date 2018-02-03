## Capstone Project Two - Playing Flappybird Using Deep Q-Networks

Introduction
======
Flappy bird is a side scrolling game where the user controls a bird and maneuvers it through the environment as it moves.  There are random pipes which are setup which the user must navigate above/below/between.  By default, the altitude of the bird decreases, and the user can tap on the screen to let it ‘flap,’ increasing its altitude for a brief moment.  Repeated taps will result in steady increase of the bird.  Hitting any of the pipes or the top/bottom of the game screen will result in termination of the trial, and score is calculated based on how far the bird was able to travel.

Approach
======
The approach for creating the policy model is two-fold: CNN to collect features from the image, and a DQN to learn policies from the resulting output from the CNN.
This is very similar to how AlphaGo was trained to play the game of Go.  

Data
=====
The flappy bird game is available to emulate via the Pygame-Learning-Environment, and there is a wrapper class available here. Together this will deal with the different termination requirements such as hitting any of the objects in the game, and provide rewards for certain action

Client
======
One possible client who may be interested in the results of this work is game designers/creators/testers.  The model could open up and enlighten customers of the game to new strategies, which can possibly help clients come up with ways to improve or make the game more difficult and enjoyable for the public.

Deliverables
======
The deliverables for this project will be the CNN and DQN models, a slidedeck presentation of the different steps taken to train these models

Notebook Descriptions
======
*data_wrangling.ipynb*: Initial data analysis is done here. There are visualizations to understand the representation of the game, data wrangling, and data generation.

*classes.py*: A python module of classes which is used for data processing.

*dqn_training.ipynb*: Creates a convolutional neural network (CNN) and trains the policy agent to learn optimal action selection policy.  Uses epsilon annealing and batch training.
