import sys
import numpy as np
from copy import deepcopy
sys.setrecursionlimit(20000000)

inital_state = [[1,2,3],[4,5,6],[7,8,0]]

goal_state = [[1,2,3],[4,5,6],[0,7,8]]

pass_state = []

#print(1)
def GBFS_init():
    GBFS(inital_state)
    
def GBFS(node):
    pass_state.append(node)
    print(node)
    if node == goal_state:
        return node
    else:
        for i in range(0,3):
            for j in range(0,3):
                if(node[i][j]==0 ):
                    if(i==0 or j==0 or i==2 or j==2):
                        if(i==0 and j==0):
                            score_board = []
                            nodeCMP = []
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode)                                
                            

                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode) 
                            
                            GBFS(nodeCMP[score_board.index(min(score_board))])
                            
                        elif(i==0 and j==2):
                            score_board = []
                            nodeCMP = []
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode) 
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode) 
                            
                            GBFS(nodeCMP[score_board.index(min(score_board))])
                            
                        elif(i==2 and j==0):
                            score_board = []
                            nodeCMP = []
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode) 
                            
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode) 
                            
                            GBFS(nodeCMP[score_board.index(min(score_board))])
                            
                        elif(i==2 and j==2):
                            score_board = []
                            nodeCMP = []
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode)                    
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode) 
                            
                            GBFS(nodeCMP[score_board.index(min(score_board))])
                            
                        elif( j==0 ):
                            score_board = []
                            nodeCMP = []                            
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode)                             
                                 
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode)                             
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode) 
                            
                            GBFS(nodeCMP[score_board.index(min(score_board))])
                            
                        elif( i==0 ):
                            score_board = []
                            nodeCMP = [] 
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode)                                                                                   
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode)                             
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode) 
                            
                            GBFS(nodeCMP[score_board.index(min(score_board))])
                            
                        elif( j==2 ):
                            score_board = []
                            nodeCMP = []                             
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode)                             
                            
       
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode)                             
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode)                             
                            
                            GBFS(nodeCMP[score_board.index(min(score_board))])
                            
                        elif( i==2 ):
                            score_board = []
                            nodeCMP = [] 
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode)                           
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode)                             
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            if( tmpNode not in pass_state):
                                score_board.append(huristic(tmpNode, goal_state))
                                nodeCMP.append(tmpNode)                             
                            
                            GBFS(nodeCMP[score_board.index(min(score_board))])
                    else:
                        score_board = []
                        nodeCMP = []                         
                        
                        tmpNode = deepcopy(node)
                        tmpNode[i][j] = tmpNode[i-1][j]
                        tmpNode[i-1][j] = 0
                        if( tmpNode not in pass_state):
                            score_board.append(huristic(tmpNode, goal_state))
                            nodeCMP.append(tmpNode) 
                        
                        tmpNode = deepcopy(node)
                        tmpNode[i][j] = tmpNode[i][j-1]
                        tmpNode[i][j-1] = 0
                        if( tmpNode not in pass_state):
                            score_board.append(huristic(tmpNode, goal_state))
                            nodeCMP.append(tmpNode) 
                        
                        #print(node)
                        tmpNode = deepcopy(node)
                        tmpNode[i][j] = tmpNode[i+1][j]
                        tmpNode[i+1][j] = 0
                        if( tmpNode not in pass_state):
                            score_board.append(huristic(tmpNode, goal_state))
                            nodeCMP.append(tmpNode) 
                        
                        tmpNode = deepcopy(node)
                        tmpNode[i][j] = tmpNode[i][j+1]
                        tmpNode[i][j+1] = 0
                        if( tmpNode not in pass_state):
                            score_board.append(huristic(tmpNode, goal_state))
                            nodeCMP.append(tmpNode)    
                        
                        GBFS(nodeCMP[score_board.index(min(score_board))])

def huristic(node, goal):
    score = 0
    for i in range(0,3):
        for j in range(0,3):
            nodecmp = node[i][j]
            for i_goal in range(0,3):
                for j_goal in range(0,3):
                    if(nodecmp==goal[i_goal][j_goal]):
                        score += abs(i-i_goal)+abs(j-j_goal)
    #print(score)
    return score
def goal_check(node):
    return node == goal_state

GBFS_init()
    
