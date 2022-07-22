#Importing the random package
import random

#Creating the Environment class
class Environment:
  def __init__(self):
    self.steps_left=10
  def get_observation(self):
    return [1.0,2.0,1.0]
  def get_actions(self):
    return [-1,1]
  def check_is_done(self):
    return self.steps_left==0
  def action(self,int):
    if self.check_is_done():
      raise Exception("Game over")
    self.steps_left-=1
    return random.random()

#Creating the Agent class
class Agent:
   def __init__(self):
     self.total_rewards=0.0
   def step(self,ob:Environment):
     curr_obs=ob.get_observation()
     print(curr_obs,end=" ")
     curr_action=ob.get_actions()
     print(curr_action)
     curr_reward=ob.action(random.choice(curr_action))
     print("curr_reward:",curr_reward)
     self.total_rewards+=curr_reward
     print("Total rewards so far= %.3f "%self.total_rewards)

if __name__=='__main__':
  obj=Environment()
  agent=Agent()
  step_number=0
  while not obj.check_is_done():
    step_number+=1
    print("Step-",step_number, end=" ")
    agent.step(obj)
  print("Total reward is %.3f "%agent.total_rewards)
