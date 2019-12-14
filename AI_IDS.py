import numpy as np
from copy import deepcopy

inital_state = [[4,1,2],[0,5,3],[8,7,6]]
goal_state = [[1,2,3],[8,0,4],[7,6,5]]

traceback_path = []

#print(1)
def IDS(node): #annace IDS function
    for depth in range(32): #depth limit 32 level, 32 is according to wikipedia max step is 4^32
        found = DLS(node, depth) #recursive DLS function
        if found != None:
            return found


def DLS(node, depth):
    #print(node)
    if depth == 0 and node == goal_state: # if level is 0 and current_node is goal
        return node
    elif depth > 0: #if depth is not 0 then recursive find the goal
        for i in range(0,3): # i is row
            for j in range(0,3): #j is column
                if(node[i][j]==0 ): # deal with the value 0 to exchange with neighbor
                    if(i==0 or j==0 or i==2 or j==2): #deal the row i = 0 or column j = 0 or row i = 2 or column = 2, the 4 side
                        if(i==0 and j==0): #deal the left top corner (0,0)
                            tmpNode = deepcopy(node) #exchange with right one(0,1) #each tmpNode is a puzzle which move one step
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp
                            
                            tmpNode = deepcopy(node) #exchange with bottom one (1,0)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp
                            
                        elif(i==0 and j==2): #deal the right top corner (0,2)
                            tmpNode = deepcopy(node)#exchange with left one (0,1)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp
                            
                            tmpNode = deepcopy(node)#exchange with bottom one (1,2)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp
                            
                        elif(i==2 and j==0):#deal the left bottom corner (2,0)
                            tmpNode = deepcopy(node)#exchange with top one (1,0)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp
                            
                            tmpNode = deepcopy(node)#exchange with right one (2,1)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp
                            
                        elif(i==2 and j==2):#deal the right bottom corner (2,2)
                            tmpNode = deepcopy(node)#exchange with top one (1,2)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp                      
                            
                            tmpNode = deepcopy(node)#exchange with left one (2,1)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp
                            
                        elif( j==0 ):#deal the left column (0,0), (1,0), (2,0)
                            tmpNode = deepcopy(node)#exchange with top one when 0 is at (1,0), (2,0)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp
                                 
                            tmpNode = deepcopy(node)#exchange with bottom one when 0 is at (0,0), (1,0)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp
                            
                            tmpNode = deepcopy(node)#exchange with right one when 0 is at (0,0), (1,0), (2,0)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp
                            
                        elif( i==0 ):#deal the top row (0,0), (0,1), (0,2)
                            tmpNode = deepcopy(node)#exchange with bottom one when 0 is at (0,0), (0,1), (0,2)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp                                                       
                            
                            tmpNode = deepcopy(node)#exchange with right one when 0 is at (0,0), (0,1)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp                              
                            
                            tmpNode = deepcopy(node)#exchange with left one when 0 is at (0,1), (0,2)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp                            
                        elif( j==2 ): #deal right column (0,2), (1,2), (2,2)
                            
                            tmpNode = deepcopy(node)#exchange with bottom one when 0 is at (0,2), (1,2)
                            tmpNode[i][j] = tmpNode[i+1][j]
                            tmpNode[i+1][j] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp
                            
       
                            tmpNode = deepcopy(node)#exchange with left one when 0 is at (0,2), (1,2), (2,2)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp                         
                            
                            tmpNode = deepcopy(node)#exchange with top one when 0 is at (1,2), (2,2)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp
                            
                        elif( i==2 ):#deal the bottom row (2,0), (2,1), (2,2)
                            tmpNode = deepcopy(node)#exchange with top one when 0 is at (2,1), (2,2)
                            tmpNode[i][j] = tmpNode[i-1][j]
                            tmpNode[i-1][j] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp                            
                            
                            tmpNode = deepcopy(node)#exchange with right one when 0 is at (2,0), (2,1)
                            tmpNode[i][j] = tmpNode[i][j+1]
                            tmpNode[i][j+1] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp  
                            
                            tmpNode = deepcopy(node)#exchange with left one when 0 is at (2,1), (2,2)
                            tmpNode[i][j] = tmpNode[i][j-1]
                            tmpNode[i][j-1] = 0
                            traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                            temp = DLS(tmpNode, depth-1)
                            if temp != None:
                                return temp                     
                    else: #deal the middle one (1,1)
                        
                        tmpNode = deepcopy(node) #exchange with top one
                        tmpNode[i][j] = tmpNode[i-1][j]
                        tmpNode[i-1][j] = 0
                        traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                        temp = DLS(tmpNode, depth-1)
                        if temp != None:
                            return temp
                        
                        tmpNode = deepcopy(node)#exchagne with left one
                        tmpNode[i][j] = tmpNode[i][j-1]
                        tmpNode[i][j-1] = 0
                        traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                        temp = DLS(tmpNode, depth-1)
                        if temp != None:
                            return temp
                        
                        #print(node)
                        tmpNode = deepcopy(node)#exchange with bottom one
                        tmpNode[i][j] = tmpNode[i+1][j]
                        tmpNode[i+1][j] = 0
                        traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                        temp = DLS(tmpNode, depth-1)
                        if temp != None:
                            return temp
                        
                        tmpNode = deepcopy(node)#exchange with right one
                        tmpNode[i][j] = tmpNode[i][j+1]
                        tmpNode[i][j+1] = 0
                        traceback_path.append([node, tmpNode]) #add current node and next node to trace array
                        temp = DLS(tmpNode, depth-1)
                        if temp != None:
                            return temp   

def goal_check(node):
    if node == goal_state :
        traceback(traceback_path, inital_state, goal_state)
    


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
    print("total steps are: "+str(len(printall)))

predic = IDS(inital_state)
goal_check(predic)
    
    