import random
from statistics import mean, pstdev
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Person:
    def __init__(self,max_step) -> None:
        self.position = 17
        self.moovement = [-1,1]
        self.max_step = max_step
        self.path = [self.position]

    def moove(self):
        for step in range(self.max_step):
            next_moove = random.choice(self.moovement)
            self.position = self.position + next_moove
            self.path.append(self.position)

            #dead case
            if self.position >= 100:
                return 1,self.position,step,self.path
            elif self.position <= 0:
                return 2,self.position,step,self.path
        
        return 0,self.position,step,self.path


MAX_STEP = 10000
NB_PERSON = 1000

morts_droite = []
morts_gauche = []
positions_vivants=[]

paths = []

for i in range(NB_PERSON):
    person = Person(MAX_STEP)
    result = person.moove()

    paths.append(result[3])

    #survive
    if result[0] ==0:
        positions_vivants.append(result[1])

    #fall on right size
    elif result[0] ==1:
        morts_droite.append(result[2])
    
    #fall on left size
    elif result[0] ==2:
        morts_gauche.append(result[2])


def animate(i):
    #plt.cla()  # Clear the current axes.
    plt.plot(paths[i])
    
    plt.title(f"Progression de {i}/{NB_PERSON} personnes dans le jeu")
    plt.xlabel('Steps')
    plt.ylabel('Position')
    plt.tight_layout()
    plt.xlim(0, MAX_STEP)
    plt.ylim(0, 100)
    
fig, ax = plt.subplots()
ani = FuncAnimation(fig, animate, frames=NB_PERSON, interval=1)

plt.show()