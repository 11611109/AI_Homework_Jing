# ghostAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from game import Agent
from game import Actions
from game import Directions
import random
from util import manhattanDistance
import util

class GhostAgent( Agent ):
    def __init__( self, index ):
        self.index = index

    def getAction( self, state ):
        dist = self.getDistribution(state)
        if len(dist) == 0:
            return Directions.STOP
        else:
            return util.chooseFromDistribution( dist )

    def getDistribution(self, state):
        "Returns a Counter encoding a distribution over actions from the provided state."
        util.raiseNotDefined()

class RandomGhost( GhostAgent ):
    "A ghost that chooses a legal action uniformly at random."
    def getDistribution( self, state ):
        dist = util.Counter()
        for a in state.getLegalActions( self.index ): dist[a] = 1.0
        dist.normalize()
        return dist

class DirectionalGhost( GhostAgent ):
    "A ghost that prefers to rush Pacman, or flee when scared."
    def __init__( self, index, prob_attack=0.8, prob_scaredFlee=0.8 ):
        self.index = index
        self.prob_attack = prob_attack
        self.prob_scaredFlee = prob_scaredFlee

    def getDistribution( self, state ):
        # Read variables from state
        ghostState = state.getGhostState( self.index )
        legalActions = state.getLegalActions( self.index )
        pos = state.getGhostPosition( self.index )
        isScared = ghostState.scaredTimer > 0

        speed = 1
        if isScared: speed = 0.5

        actionVectors = [Actions.directionToVector( a, speed ) for a in legalActions]
        newPositions = [( pos[0]+a[0], pos[1]+a[1] ) for a in actionVectors]
        pacmanPosition = state.getPacmanPosition()

        # Select best actions given the state
        distancesToPacman = [manhattanDistance( pos, pacmanPosition ) for pos in newPositions]
        if isScared:
            bestScore = max( distancesToPacman )
            bestProb = self.prob_scaredFlee
        else:
            bestScore = min( distancesToPacman )
            bestProb = self.prob_attack
        bestActions = [action for action, distance in zip( legalActions, distancesToPacman ) if distance == bestScore]

        # Construct distribution
        dist = util.Counter()
        for a in bestActions: dist[a] = bestProb / len(bestActions)
        print (dist)
        print ("line/////////")
        for a in legalActions: dist[a] += ( 1-bestProb ) / len(legalActions)
        print (dist)
        dist.normalize()
        return dist



def scoreEvaluationFunctionGhost(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """

    return currentGameState.getScore()
#

class MinimaxGhost(GhostAgent):


    "*** YOUR CODE HERE ***"
    def __init__(self, index, evalFn = 'scoreEvaluationFunctionGhost', depth = '2'):
        self.index = index # Ghosts are always agent index > 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction
          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.

        """
        minimum = []
        actions = []

        for action in gameState.getLegalActions(self.index):
            finalMin = self.minimax(gameState, self.index,1,self.index)
            if action is not Directions.STOP:
                minimum.append(finalMin)
                actions.append(action)
        finalScore = min(minimum)
        indexSet=[]
        for i in range(len(minimum)):
            if minimum[i]==finalScore:
                indexSet.append(i)
        randomAc = random.choice(indexSet)
        return actions[randomAc]

    def minimax(self, gameState, agent, depth,currentGhost):
        if depth == self.depth or gameState.isWin() or gameState.isLose() and depth!=1:
            return self.evaluationFunction(gameState)
        moves = gameState.getLegalActions(agent)
        if agent==currentGhost:
            scores = [self.minimax(gameState.generateSuccessor(agent, move), 0, depth, currentGhost) for move in
                      moves]
            final=max(scores,"-inf")
        else:
            scores = [
                self.minimax(gameState.generateSuccessor(agent, move), currentGhost, (depth + 1), currentGhost) for
                move in moves]
            final = min(scores, "inf")
        return final