import requests
import networkx
import math
import functools
SESSION_COOKIE = "53616c7465645f5f00eb92e40c3e8203648e23ee072ce796e6eb04a8d61ee84aa95c898be3d3a6f0fe29ca362d6f9dcfbaf99c873f0631df63f6f39d4096e489"
response = requests.get("https://adventofcode.com/2025/day/8/input", cookies = {'session': SESSION_COOKIE})

if response.status_code == 200:
    input = response.text
else:
    print(f"Error: {response.status_code}")

input = input.splitlines()
connections = 1000

G = networkx.Graph()
for i, box in enumerate(input):
    x, y, z = box.split(',')
    G.add_node(i, x=int(x), y=int(y), z=int(z))

T = G.copy()

for node1 in G:
    for node2 in G:
        if node1==node2:
            continue
        else:
            dispx = abs(G.nodes[node1]['x'] - G.nodes[node2]['x'])
            dispy = abs(G.nodes[node1]['y'] - G.nodes[node2]['y'])
            dispz = abs(G.nodes[node1]['z'] - G.nodes[node2]['z'])
            dist = math.sqrt(dispx**2 + dispy**2 + dispz**2)
            G.add_edge(node1, node2, dist=dist)

kruskal_edges = sorted(G.edges(data=True), key= lambda x: x[2].get('dist',0))

for i in range(connections):
    #i didn't want to implement a union find data structure so this is O(V^2)
    if not networkx.has_path(T,kruskal_edges[i][0], kruskal_edges[i][1]):
        T.add_edge(kruskal_edges[i][0],kruskal_edges[i][1])

ccs = networkx.connected_components(T)

total = 0
largest = [0 for _ in range(3)]
for cc in ccs:
    total += len(cc)
    i = 0
    while i <= 2 and len(cc) < largest[i]:
        i += 1
    if i != 3:
        largest.insert(i, len(cc))
        largest.pop()

print(total) #sanity check
print(largest)
print(functools.reduce(lambda x, y: x*y, largest))

