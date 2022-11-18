import sys
import json
import ast
from graph import Graph as g
from dfs import rechercheBFS as DFS
from bfs import rechercheDFS as BFS

input = ast.literal_eval(sys.argv[1])
newGraph = g(input, [], {})
nodes = newGraph.convertToGraph()

startNode = int(sys.argv[2])
methode = int(sys.argv[3])

result = None
if methode == 1:
    recherchedFS = DFS(nodes, startNode)
    result = recherchedFS.recherche()

if methode == 2:
    recherchebFS = BFS(nodes, startNode)
    result = recherchebFS.recherche()

print(json.dumps(result))

sys.stdout.flush()