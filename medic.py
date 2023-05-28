import json
import random
from loguru import logger
from spade.behaviour import OneShotBehaviour
from spade.template import Template
from spade.message import Message
from pygomas.bditroop import BDITroop
from pygomas.bdimedic import BDIMedic
from pygomas.bdifieldop import BDIFieldOp
from agentspeak import Actions
from agentspeak import grounded
from agentspeak.stdlib import actions as asp_action
from pygomas.ontology import DESTINATION

from pygomas.agent import LONG_RECEIVE_WAIT

class BDIDrunkenMedic(BDIMedic):
    def add_custom_actions(self, actions):
        super().add_custom_actions(actions)
    

        @actions.add_function(".calculateFormation", (tuple) )
        def _calculateFormation(Pos):
            maxX = 15
            maxZ = 15
            randX = random.randrange(0, maxX)
            randZ = random.randrange(0, maxZ)

            while (self.map.can_walk(randX, randZ) == False):
                randX = random.randrange(0, 15)
                randZ = random.randrange(0, 15)

            return (randX + Pos[0], 0, randZ + Pos[2])
        
        @actions.add_function(".calculateDest", (tuple) )
        def _calculateDest(Pos):
            randX = random.randrange(0, 10)
            randZ = random.randrange(0, 10)

            while (self.map.can_walk(randX, randZ) == False):
                randX = random.randrange(0, 10)
                randZ = random.randrange(0, 10)

            return (Pos[0] - randX, 0, Pos[2] - randZ)