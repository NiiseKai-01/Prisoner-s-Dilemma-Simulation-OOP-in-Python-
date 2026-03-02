#All player classes in here
import random

#main parent class for all strategies
class player:
    all_players=[]
    def __init__(self,name):
        self.name=name
        self.rewards=0
        self.opponent_last_moves=[]
        player.all_players.append(self)
    def act(self):
        raise NotImplementedError("Subclasses must implement act()")
    def __str__(self):
        return f"Name = {self.name}, Strategy = {self.__class__.__name__}, Total reward = {self.rewards}, Opponents last moves = {self.opponent_last_moves}"                


class always_cooperate(player):
    #not needed necessarily if dont want additional changes in init function from parent method
    def __init__(self,name):
        super().__init__(name)
    def act(self):
        return 1
#Test for always cooperating player
# x=always_cooperate("alice")
# print(x.act(),x)


class always_defect(player):
    def act(self):
        return 0
#Test for always defecting player
# x=always_defect("Bob")
# print(x)


class titfortat(player):
    def act(self):
        return 1 if not self.opponent_last_moves else self.opponent_last_moves[-1]
#Test for titfortat player
# x=titfortat("punisher")
# print(x.act())
# x.opponent_last_moves=np.append(x.opponent_last_moves,[])
# print(x.act())
# print(x)


class Random(player):
    def act(self):
        return random.choice([0,1])
#Test for random selecting player
# x=Random("creep")
# print(x.act())
# print(x)


class Grim_trigger(player):
    def __init__(self,name):
        super().__init__(name)
        self.trigger=0
    def act(self):
        if self.opponent_last_moves and self.opponent_last_moves[-1]==0:
            self.trigger=1
        return 0 if self.trigger==1 else 1
#Test for GRIM trigger player
# x=Grim_trigger("Dave")
# print(x)
# print(x.act())
# x.opponent_last_moves=np.append(x.opponent_last_moves,0)
# print(x.act())
# print(x.act())