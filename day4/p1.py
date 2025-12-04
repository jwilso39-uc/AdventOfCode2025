import requests
SESSION_COOKIE = "53616c7465645f5f00eb92e40c3e8203648e23ee072ce796e6eb04a8d61ee84aa95c898be3d3a6f0fe29ca362d6f9dcfbaf99c873f0631df63f6f39d4096e489"
response = requests.get("https://adventofcode.com/2025/day/4/input", cookies = {'session': SESSION_COOKIE})

if response.status_code == 200:
    input = response.text
else:
    print(f"Error: {response.status_code}")

def calc_neighbors(rows, row, col):
    neighbors = 0
    for i in range(row-1,row+2):
        for j in range(col-1, col+2):
            if i>=0 and i<len(rows) and j>=0 and j<len(rows[0]) and not (i == row and j == col):
                if rows[i][j] == '@':
                    neighbors += 1
    return neighbors

rows = input.splitlines()

available = 0
round_total = 1

while round_total >0:
    round_total = 0
    for i, row in enumerate(rows):
        for j, roll in enumerate(row):
            if roll == '@':
                neighbors = calc_neighbors(rows,i,j)
                if neighbors < 4:
                    round_total += 1
                    rows[i] = rows[i][:j] + 'x' + rows[i][j+1:]
    available += round_total

print(available)
