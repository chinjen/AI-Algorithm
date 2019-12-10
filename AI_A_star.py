import sys
import numpy as np
from copy import deepcopy
sys.setrecursionlimit(2000000000)

inital_state = [[1,2,3],[8,4,5],[0,7,6]]

goal_state = [[1,2,3],[8,0,4],[7,6,5]]

pass_state = []
score_board = []
scoreNode = []

#print(1)
def A_star_init():
    A_star(inital_state)
    
def A_star(node):
    global score_board, scoreNode
    pass_state.append(node) #add node to pass state to avoid same state
    print(node)
    if node == goal_state:
        return node
    else:
        for i in range(0,3):
            for j in range(0,3):
                if(node[i][j]==0 ):
                    if(i==0 or j==0 or i==2 or j==2):
                        if(i==0 and j==0):
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                #compurt current node and the inital distance = g(n) value and current node and goal distance = h(n) value and add to socre board
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state)) 
                                scoreNode.append(tmpNode) #add node to score node                               
                            

                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode) 
                            
                            score_index = score_board.index(min(score_board)) #find the minimum f(n) = g(n)+h(n)
                            score_board.pop(score_index) #take this minimum value out
                            A_star(scoreNode.pop(score_index)) #continue do A* search on node which has minimum f value
                            
                        elif(i==0 and j==2):
                         
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode)  
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode)  
                            
                            score_index = score_board.index(min(score_board))
                            score_board.pop(score_index)
                            A_star(scoreNode.pop(score_index))
                            
                        elif(i==2 and j==0):
                         
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode)  
                            
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode) 
                            
                            score_index = score_board.index(min(score_board))
                            score_board.pop(score_index)
                            A_star(scoreNode.pop(score_index))
                            
                        elif(i==2 and j==2):
                         
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode)                    
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode) 
                            
                            score_index = score_board.index(min(score_board))
                            score_board.pop(score_index)
                            A_star(scoreNode.pop(score_index))
                            
                        elif( j==0 ):
                                                     
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode)                             
                                 
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode)                             
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode) 
                            
                            score_index = score_board.index(min(score_board))
                            score_board.pop(score_index)
                            A_star(scoreNode.pop(score_index))
                            
                        elif( i==0 ):
                          
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode)                                                                                   
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode)                             
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode) 
                            
                            score_index = score_board.index(min(score_board))
                            score_board.pop(score_index)
                            A_star(scoreNode.pop(score_index))
                            
                        elif( j==2 ):
                                                      
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode)                             
                            
       
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode)                             
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode)                             
                            
                            score_index = score_board.index(min(score_board))
                            score_board.pop(score_index)
                            A_star(scoreNode.pop(score_index))
                            
                        elif( i==2 ):
                          
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode)                           
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode)                             
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            if( tmpNode not in pass_state): #this node is not is the previous pass state
                                score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                                scoreNode.append(tmpNode)                             
                            
                            score_index = score_board.index(min(score_board))
                            score_board.pop(score_index)
                            A_star(scoreNode.pop(score_index))
                    else:
                        score_board = []
                        nodeCMP = []                         
                        
                        tmpNode = deepcopy(node)
                        tmpNode[i][j] = tmpNode[i-1][j]
                        tmpNode[i-1][j] = 0
                        if( tmpNode not in pass_state): #this node is not is the previous pass state
                            score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                            scoreNode.append(tmpNode)   
                        
                        tmpNode = deepcopy(node)
                        tmpNode[i][j] = tmpNode[i][j-1]
                        tmpNode[i][j-1] = 0
                        if( tmpNode not in pass_state): #this node is not is the previous pass state
                            score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                            scoreNode.append(tmpNode)
                        
                        #print(node)
                        tmpNode = deepcopy(node)
                        tmpNode[i][j] = tmpNode[i+1][j]
                        tmpNode[i+1][j] = 0
                        if( tmpNode not in pass_state): #this node is not is the previous pass state
                            score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                            scoreNode.append(tmpNode) 
                        
                        tmpNode = deepcopy(node)
                        tmpNode[i][j] = tmpNode[i][j+1]
                        tmpNode[i][j+1] = 0
                        if( tmpNode not in pass_state): #this node is not is the previous pass state
                            score_board.append(huristic(inital_state, tmpNode)+huristic(tmpNode, goal_state))
                            scoreNode.append(tmpNode)    
                        
                        score_index = score_board.index(min(score_board))
                        score_board.pop(score_index)
                        A_star(scoreNode.pop(score_index))

def huristic(node, goal): #manhatom algorithm
    score = 0
    for i in range(0,3):
        for j in range(0,3):
            nodecmp = node[i][j] #current node position value
            for i_goal in range(0,3):
                for j_goal in range(0,3):
                    if(nodecmp==goal[i_goal][j_goal]): #if current node == expect node position value
                        score += abs(i-i_goal)+abs(j-j_goal) #x position cut each and y position cut each other
    #print(score)
    return score
def goal_check(node):
    return node == goal_state

A_star_init()
    
