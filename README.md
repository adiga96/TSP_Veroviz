# Vehicle Route optimization using Veroviz

Travelling Salesman Problem using nearest neighbour and simulated annealing heurisitcs

The function solveTSP_SA accepts 3 inputs:

1. nodesDF: A VeRoViz nodes dataframe containing n locations, numbered 1 to n. Location 1 is assumed as the home location.

VeRoViz is an open-source project from the Optimator Lab, in the University at Buffalo's Department of Industrial & Systems Engineering
The aim of VeRoViz is to help users to obtain road network data, sketch the locations of nodes (e.g. customers and depots), 
visualize arcs (connections) among these nodes, generate 3D movies show casing solutions to vehicle routing problems, quickly generate test
problems and distance (and/or time) matrices.


2. costDict – A VeRoViz “time” dictionary describing either the travel time, in seconds, from each node to every other node.
The contents of costDict will be generated by the VeRoViz getTimeDist2D() function which is an input to our function and this there is
no need to calculate this dictionary. The travel time values will be generated using the “ORS-online” dataProvider.
Documentation on the “time” dictionary may be found at https://veroviz.org/docs/veroviz.getTimeDist2D.html. 

Documentationonthe“ORS-online”dataprovidermaybefoundathttps://veroviz. org/docs/dataproviders.html.

3. timeLimit – A scalar value describing the maximum runtime of your heuristic, in units of seconds
The solveTSP_SA returns a VeRoViz “assignments” dataframe, as described here: https://veroviz.org/docs/assignments.html
