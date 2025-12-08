import requests
SESSION_COOKIE = "53616c7465645f5f00eb92e40c3e8203648e23ee072ce796e6eb04a8d61ee84aa95c898be3d3a6f0fe29ca362d6f9dcfbaf99c873f0631df63f6f39d4096e489"
response = requests.get("https://adventofcode.com/2025/day/7/input", cookies = {'session': SESSION_COOKIE})

if response.status_code == 200:
    input = response.text
else:
    print(f"Error: {response.status_code}")

input = input.splitlines()

#bottom up DP solution, need timelines one for each possible beam:
#base states is one timeline in last row for each beam
DP = [1 for _ in range(len(input[0]))]

for i in range(len(input)-2, -1, -1):
    new_dp = []
    for j in range(len(input[i])):
        if input[i][j] == '^':
            new_dp.append(DP[j-1] + DP[j+1])
        else:
            new_dp.append(DP[j])
    DP = new_dp.copy()

print(DP[input[0].find('S')])