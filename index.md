## Project Summary

Our project would like to train a regular Minecraft player to be able to learn about and defeat the Ender Dragon. The Ender Dragon is treated as the final boss of the game and as such it is a difficult task to complete. We are hoping to train an agent and see if it will be able to adapt to the various phases of the boss fight. The agent will attempt to use all of the tools at its disposal, analyze its environment, and the behavior of the ender dragon as its inputs. Its outputs will be various actions and/or series of actions that it will take in response to its inputs. We would also like to see if the agent would end up finding more optimal techniques about how to slay the dragon than what humans currently do. 

This major task has a variety of sub tasks that the agent will need to learn optimally in order to skillfully defeat the dragon. 

## Evaluation Plan

Below are the quantitative measures we will be looking at to rate the performance of our engine. We will be looking to minimize the use of the resources we give the agent, maximize the agent health at the end of the battle, minimize the amount of health lost by the agent, and minimize the time taken to defeat the dragon. The baseline for the measurements will be as follows. Using up to 20 resources, having full health at the end, losing 0 hearts throughout the fight, and taking a maximum of 15 minutes to defeat the dragon. 
 
For the qualitative measures, we will have a variety of subtasks and methods of evaluating these subtasks to make sure that the agent is making continuous progress. Throughout the project we will do reward shaping, for example we will first reward the agent for destroying the pillars that will allow the agent to actually start doing damage to the ender dragon. To make sure that our approach is working, we will periodically save the current model’s weights and manually assess the current model’s weights to determine whether or not it is making any progress. The moonshot case is that the agent figures out how to slay the dragon in less time than the current human world record (1 minute and 30 seconds). 

## Goals

#### Minimum Goal 
The minimum goal we should be able to achieve is to have the agent learn the various subtasks that will be at play and that the agent needs to do in order to beat the ender dragon.

Milestone 1:
The agent is able to aim and shoot all pillars that are shootable with 100% accuracy and is able to climb up to the pillars that are surrounded by fences and destroy them as well. The agent will have damage resist during this phase. 
 
Milestone 2:
The agent is able to aim and shoot at the dragon while it flies in the air and engage the dragon in melee combat. The agent will have damage resist during this phase. 
 
#### Realistic Goal
The realistic goal would be to have the agent learn how to switch between its various subtasks in order to defeat the ender dragon while having a heavy damage resistance (the agent is much harder to kill). 

Milestone 1:
The agent is able to switch from the shooting the pillars mode to the climbing up to and destroying the pillars mode flawlessly. The agent will have damage resist during this phase. 
 
Milestone 2:
The agent is able to optimally switch from all of the subtasks it has trained on in order to defeat the ender dragon within 15 minutes. The agent will have damage resist during this phase. 
 
#### Ambitious Goal
The ambitious goal would be to have the agent be able to defeat the ender dragon quicker than the human world record while taking regular amounts of damage. 

Milestone 1:
The agent is able to beat the dragon while taking regular amounts of damage and is able to beat and/or come close to the current human record time (1 minute and 30 seconds) held for defeating the ender dragon.
