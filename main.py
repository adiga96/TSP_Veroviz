#!/usr/bin/env python
# coding: utf-8

def solveTSP_SA(nodesDF, costDict, timeLimit):
    
    ORS_API_KEY = '5b3ce3597851110001cf6248cd17d3535dc040458d794031286771a4'
    
    def solve_tsp_nn(startNode, costDict, nodesDF): 
        """
        This function computes a "nearest neighbor" solution to a TSP.

        Inputs
        ------
        startNode: Integer, indicating the node where the salesperson begins (and ends) the route

        costDict: VeRoViz time or distance dictionary.

        nodesDF: VeRoViz nodes dataframe

        Returns
        -------
        An ordered list of nodeIDs specifying a TSP route.
        """
        startNode = 1
        # Solve the TSP with a "nearest neighbor" heuristic
        nn_route = []

        # Start our route by visiting the startNode
        nn_route.append(startNode)

        # Initialize a list of unvisited nodes
        unvisitedNodes = list(nodesDF[nodesDF['id'] != startNode]['id'])

        # Let i represent our "current" location:
        i = startNode

        while len(unvisitedNodes) > 0:
            # Initialize minTime to a huge value
            minTime = float('inf')

            # Find the nearest unvisited node to our current node:
            for j in unvisitedNodes:
                if (costDict[i,j] < minTime):
                    nextNode = j
                    minTime = costDict[i,j]

            # Update our salesperson's location
            i = nextNode

            # Append nextNode to our route:
            nn_route.append(nextNode)

            # Remove nextNode from our list of unvisitedNodes:
            unvisitedNodes.remove(nextNode)

        nn_route.append(startNode)

        return nn_route    
    
# Calculating Cost Function
    def tsp_cost(route, costDict):
        cost = 0

        i = route[0]
        for j in route[1:]:
            cost += costDict[i,j]
            i = j

        cost += costDict[i, route[0]]

        return cost

#Reversal Neighbor Fucntion 
    import random
    import math
    import time
    myList = solve_tsp_nn(1, costDict, nodesDF)
    
    def tsp_neighbor(route):
        

        a = random.randint(0,len(myList)-3)
        b = random.randint(a+1, len(myList)-2)

        newRoute = []
        newRoute.extend(route[0:a])

        subtour = route[a:b+1]
        subtour.reverse()
        newRoute.extend(subtour)

        newRoute.extend(route[b+1:len(route)-1])

        newRoute.append(newRoute[0])

        return newRoute
    
#Initialising Values
    
    T0 = 100000    # Initial Temperature
    I = 20
    delta = 2000  #temp after which sudden cooling occurs
    T_final = 500
    Cutoff_time = timeLimit  # Time Limit describing MAX RUN TIME 
    
    
#Initial Solution assignment for Nearest Neighbour function

    X0 = solve_tsp_nn(1, costDict, nodesDF) # Initial Solution
    Xcur = X0    # Current Solution = Initial Solution from Nearest Neighbour Solution
    X_best = Xcur
    Z_cur = tsp_cost(X0, costDict) 
#     Xcur, Z_cur
    
#Solution assignment from TSP Neighbour function
    Xcount = tsp_neighbor(myList)
    Z_Xcount = tsp_cost(Xcount,costDict)
#     Xcount, Z_Xcount
    
#PHASE II Simmulated Anealing
    T_cur = T0 
    Z_best = Z_cur
    count = 1   # Initialising Count value to 1
    while count <= I:         # I is the number of iterations per temperature
        if(Z_Xcount < Z_cur):

            Xcur = Xcount
            Z_cur = Z_Xcount
    #         print("1st",Xcur)
    #         print("1st",Z_cur)
        else:
            del_C = Z_Xcount - Z_cur
            if(random.random() <= math.exp( -del_C / T_cur)):
                Xcur = Xcount
                Z_cur = Z_Xcount
    #             print("2nd",Xcur)
    #             print("2nd",Z_cur)


        if (tsp_cost(X0, costDict) < Z_best):
                Z_best = tsp_cost(X0, costDict)
                X_best = Xcur
    #             print("3rd",Z_best)
    #             print("3rd",X_best)

# PHASE III Simmulated Anealing
        
        T_cur = T_cur - delta
    #     print("after", T_cur, T_final)

        if((T_cur < T_final) or ((time.time() + Cutoff_time) - time.time() == 0)):
            break
        else:
            count+=1
        
# Creating assigmentsDF = Output of solveTSP_SA
    import veroviz as vrv
    import urllib3
    urllib3.disable_warnings()
   
    assignmentsDF = vrv.createAssignmentsFromNodeSeq2D(
    nodeSeq          = X_best,        # This is what you should have found above, via SA.
    nodes            = nodesDF,       # This is an input to your solveTSP_SA() function
    routeType        = 'fastest',     # Leave this as 'fastest'
    dataProvider     = 'ORS-online',  # Leave this as 'ORS-online'
    dataProviderArgs = {'APIkey' : ORS_API_KEY})    # You'll need to replace ORS_API_KEY with your actual key
    
    return assignmentsDF
