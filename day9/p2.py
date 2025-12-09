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
verts = dict()
horz = dict()
for i, tile in enumerate(input):
    x, y = tile.split(',')
    G.add_node(i, x=int(x), y=int(y))
    #store vertical/horizontal edges
    if i != 0 and G.nodes[i-1]['x'] == G.nodes[i]['x']:
        verts[G.nodes[i]['x']] = sorted([G.nodes[i-1]['y'], G.nodes[i]['y']])
    if i != 0 and G.nodes[i-1]['y'] == G.nodes[i]['y']:
        horz[G.nodes[i]['y']] = sorted([G.nodes[i-1]['x'], G.nodes[i]['x']])
    #loop around
    if i == len(input) - 1 and G.nodes[0]['x'] == G.nodes[i]['x']:
        verts[G.nodes[i]['x']] = sorted([G.nodes[i]['y'], G.nodes[0]['y']])
    if i == len(input) - 1 and G.nodes[0]['y'] == G.nodes[i]['y']:
        horz[G.nodes[i]['y']] = sorted([G.nodes[i]['x'], G.nodes[0]['x']])

def all_tiles_green(node1, node2):
    ll = [(G.nodes[node1]['x'],G.nodes[node1]['y']), (G.nodes[node1]['x'],G.nodes[node2]['y']), (G.nodes[node2]['x'],G.nodes[node1]['y']), (G.nodes[node2]['x'],G.nodes[node2]['y'])]
    ll.sort()
    aa, ab, ba, bb = ll

    for col in [col for key, col in verts.items() if key>aa[0] and key<ba[0]]:
        #bottom edge
        if col[0] <= aa[1] and col[1] > aa[1]:
            return False
        #top edge
        elif col[0] < ab[1] and col[1] >= ab[1]:
            return False
    for row in [row for key, row in horz.items() if key>aa[1] and key<ab[1]]:
        #left edge
        if row[0]<=aa[0] and row[1]>aa[0]:
            return False
        #right edge
        if row[0]<ba[0] and row[1]>ba[0]:
            return False

    #all edges good
    return True
        

for node1 in G:
    for node2 in G:
        if node1==2 and node2==6:
            print("here")
        if node2<=node1:
            continue
        elif all_tiles_green(node1,node2):
            dispx = abs(G.nodes[node1]['x'] - G.nodes[node2]['x'])+1
            dispy = abs(G.nodes[node1]['y'] - G.nodes[node2]['y'])+1
            area = dispx*dispy
            G.add_edge(node1, node2, area=area)

kruskal_edges = sorted(G.edges(data=True), key= lambda x: x[2].get('area',0))

print(G.nodes[kruskal_edges[-1][0]],G.nodes[kruskal_edges[-1][1]])
print(kruskal_edges[-1])