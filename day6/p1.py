import requests
import functools
SESSION_COOKIE = "53616c7465645f5f00eb92e40c3e8203648e23ee072ce796e6eb04a8d61ee84aa95c898be3d3a6f0fe29ca362d6f9dcfbaf99c873f0631df63f6f39d4096e489"
response = requests.get("https://adventofcode.com/2025/day/6/input", cookies = {'session': SESSION_COOKIE})

if response.status_code == 200:
    input = response.text
else:
    print(f"Error: {response.status_code}")

input = input.splitlines()

math = [[] for _ in range(len(input))]

for i, line in enumerate(input):
    if i != len(input)-1:
        math[i] = list(map(int, line.split()))
    else:
        math[i] = line.split()
    

total = 0
for i, symbol in enumerate(math[-1]):
    if symbol == "*":
        answer = functools.reduce(lambda a, b: a * b, [row[i] for j, row in enumerate(math) if j!=len(math)-1])
    else:
        answer = functools.reduce(lambda a, b: a + b, [row[i] for j, row in enumerate(math) if j!=len(math)-1])
    total += answer

print(total)