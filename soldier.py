import json
import random
from loguru import logger
from spade.behaviour import OneShotBehaviour
from spade.template import Template
from spade.message import Message
from pygomas.bditroop import BDITroop
from pygomas.bdifieldop import BDIFieldOp
from agentspeak import Actions
from agentspeak import grounded
from agentspeak.stdlib import actions as asp_action
from pygomas.ontology import DESTINATION

from pygomas.agent import LONG_RECEIVE_WAIT

class BDIDrunkenSoldier(BDITroop):
    def add_custom_actions(self, actions):
        super().add_custom_actions(actions)
    

        @actions.add_function(".calculateFormation", (tuple) )
        def _calculateFormation(Pos):
            signo = random.randrange(0, 2)

            maxX = 40
            maxZ = 40
            randX = random.randrange(5, maxX)
            randZ = random.randrange(5, maxZ)

            if (signo == 0):
                randX = Pos[0] - randX
                randZ = Pos[2] + randZ
            else:
                randX = Pos[0] + randX
                randZ = Pos[2] - randZ  


            while (self.map.can_walk(randX, randZ) == False):
                randX = random.randrange(5, maxX, 3)
                randZ = random.randrange(5, maxZ, 3)

                if (signo == 0):
                    randX = Pos[0] - randX
                    randZ = Pos[2] + randZ
                else:
                    randX = Pos[0] + randX
                    randZ = Pos[2] - randZ  

            return (randX, 0, randZ)
        
        @actions.add_function(".calculateDest", (tuple) )
        def _calculateDest(Pos):
            signo = random.randrange(0, 2)

            randX = random.randrange(0, 15, 1)
            randZ = random.randrange(0, 15, 1)

            if (signo == 0):
                randX = Pos[0] - randX
                randZ = Pos[2] + randZ
            else:
                randX = Pos[0] + randX
                randZ = Pos[2] - randZ  


            while (self.map.can_walk(randX, randZ) == False):
                randX = random.randrange(0, 15, 3)
                randZ = random.randrange(0, 15, 3)

                if (signo == 0):
                    randX = Pos[0] - randX
                    randZ = Pos[2] + randZ
                else:
                    randX = Pos[0] + randX
                    randZ = Pos[2] - randZ  

            return (randX, 0, randZ)