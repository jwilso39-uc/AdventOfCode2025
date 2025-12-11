import requests
import networkx as nx
SESSION_COOKIE = "53616c7465645f5f00eb92e40c3e8203648e23ee072ce796e6eb04a8d61ee84aa95c898be3d3a6f0fe29ca362d6f9dcfbaf99c873f0631df63f6f39d4096e489"
response = requests.get("https://adventofcode.com/2025/day/11/input", cookies = {'session': SESSION_COOKIE})

if response.status_code == 200:
    input = response.text
else:
    print(f"Error: {response.status_code}")

def dfs_visit(G: nx.DiGraph, u, node2, memo, onpath):
    #memoization
    if memo.get(u) is not None:
        return memo[u]
    paths = 0
    for v in G.neighbors(u):
        if v == node2:
            paths += 1
        elif v in onpath:
            paths += dfs_visit(G, v, node2, memo, onpath)
    memo[u] = paths
    return paths

#boo i actually need to do optimizations
def find_all_paths(G: nx.DiGraph, node1: str, node2: str):
    onpath = set()
    edges = nx.bfs_edges(G, node2, reverse=True)
    for edge in edges:
        onpath.add(edge[0])
        onpath.add(edge[1])
    memo = dict()
    return dfs_visit(G, node1, node2, memo, onpath)


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

#run DFS and find all paths for all needed
svr_dac = find_all_paths(G, "svr", "dac")
dac_fft = find_all_paths(G, "dac", "fft")
fft_dac = find_all_paths(G, "fft", "dac")
svr_fft = find_all_paths(G, "svr", "fft")
dac_out = find_all_paths(G, "dac", "out")
fft_out = find_all_paths(G, "fft", "out")

#combanatorics to get solution
tot1 = svr_dac * dac_fft * fft_out
tot2 = svr_fft * fft_dac * dac_out

total = tot1 + tot2
print(total)