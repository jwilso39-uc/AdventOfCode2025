import requests
import networkx as nx
SESSION_COOKIE = "53616c7465645f5f00eb92e40c3e8203648e23ee072ce796e6eb04a8d61ee84aa95c898be3d3a6f0fe29ca362d6f9dcfbaf99c873f0631df63f6f39d4096e489"
response = requests.get("https://adventofcode.com/2025/day/11/input", cookies = {'session': SESSION_COOKIE})

if response.status_code == 200:
    input = response.text
else:
    print(f"Error: {response.status_code}")

input = input.splitlines()

G = nx.DiGraph()
#add vertices
for box in input:
    node = box.split(":")
    G.add_node(node[0])

#add edges
for box in input:
    data = box.split(":")
    node = data[0]
    links = data[1]
    for link in links.split():
        G.add_edge(node, link)

#run DFS and find all paths
total = 0
for path in nx.all_simple_paths(G,"svr","dac"):
    total += 1

print(total)
    