import numpy as np
from copy import deepcopy

inital_state = [[1,2,3],[8,6,4],[7,0,5]]

goal_state = [[1,2,3],[8,0,4],[7,6,5]]


queue = []
traceback_path = []
#print(1)
def uninform_cost_searsh():
    queue.append(inital_state) #add 
    while(queue):
        temp = BFS(queue.pop(0))
        if temp != None:
            traceback(traceback_path, inital_state, goal_state)
            break 
    
def BFS(node):
    #print(node)
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
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)

                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)
                            
                        elif(i==0 and j==2):
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)
                            
                        elif(i==2 and j==0):
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)
                            
                        elif(i==2 and j==2):
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)                      
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)
                            
                        elif( j==0 ):
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)
                                 
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)                           
                        elif( i==0 ):
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)                                                       
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)                              
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)                            
                        elif( j==2 ):
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)
                            
       
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)                         
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)
                            
                        elif( i==2 ):
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)                            
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)  
                            
                            tmpNode = deepcopy(node)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            traceback_path.append([node, tmpNode])
                            queue.append(tmpNode)                     
                    else:
                        
                        tmpNode = deepcopy(node)
                        tmpNode[i][j] = tmpNode[i-1][j]
                        tmpNode[i-1][j] = 0
                        traceback_path.append([node, tmpNode])
                        queue.append(tmpNode)
                        
                        tmpNode = deepcopy(node)
                        tmpNode[i][j] = tmpNode[i][j-1]
                        tmpNode[i][j-1] = 0
                        traceback_path.append([node, tmpNode])
                        queue.append(tmpNode)
                        
                        #print(node)
                        tmpNode = deepcopy(node)
                        tmpNode[i][j] = tmpNode[i+1][j]
                        tmpNode[i+1][j] = 0
                        traceback_path.append([node, tmpNode])
                        queue.append(tmpNode)
                        
                        tmpNode = deepcopy(node)
                        tmpNode[i][j] = tmpNode[i][j+1]
                        tmpNode[i][j+1] = 0
                        traceback_path.append([node, tmpNode])
                        queue.append(tmpNode)   
            
        
def traceback(traceback_path, init, goal):
    printinit = deepcopy(goal) #first trace target is your final goal
    printall = [] # a array to record all path
    printall.append(goal) # record goal first
    while printinit != init: #loop until find the init node
        for item in traceback_path: #loop path array
            if(item[1] == printinit): #if the last is found
                printinit = item[0] #target to the previous node
                printall.append(item[0]) #input previous node to all path
                break
    printall.reverse() #oppsidedown all path
    for item in printall: #print all path
        print(item)
        
def goal_check(node):
    return node == goal_state

uninform_cost_searsh()
    
