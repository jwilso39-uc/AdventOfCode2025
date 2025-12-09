import requests
import networkx
SESSION_COOKIE = "53616c7465645f5f00eb92e40c3e8203648e23ee072ce796e6eb04a8d61ee84aa95c898be3d3a6f0fe29ca362d6f9dcfbaf99c873f0631df63f6f39d4096e489"
response = requests.get("https://adventofcode.com/2025/day/9/input", cookies = {'session': SESSION_COOKIE})

if response.status_code == 200:
    input = response.text
else:
    print(f"Error: {response.status_code}")

input = input.splitlines()

G = networkx.Graph()
for i, tile in enumerate(input):
    x, y = tile.split(',')
    G.add_node(i, x=int(x), y=int(y))

for node1 in G:
    for node2 in G:
        if node1==node2:
            continue
        else:
            dispx = abs(G.nodes[node1]['x'] - G.nodes[node2]['x'])+1
            dispy = abs(G.nodes[node1]['y'] - G.nodes[node2]['y'])+1
            area = dispx*dispy
            G.add_edge(node1, node2, area=area)

kruskal_edges = sorted(G.edges(data=True), key= lambda x: x[2].get('area',0))

print(G.nodes[kruskal_edges[-1][0]],G.nodes[kruskal_edges[-1][1]])
print(kruskal_edges[-1])