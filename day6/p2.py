import requests
import functools
SESSION_COOKIE = "53616c7465645f5f00eb92e40c3e8203648e23ee072ce796e6eb04a8d61ee84aa95c898be3d3a6f0fe29ca362d6f9dcfbaf99c873f0631df63f6f39d4096e489"
response = requests.get("https://adventofcode.com/2025/day/6/input", cookies = {'session': SESSION_COOKIE})

if response.status_code == 200:
    input = response.text
else:
    print(f"Error: {response.status_code}")

input = input.splitlines()

problems = [[]]

args = input[-1].split()
args.reverse()

for i in range(len(input[0])-1,-1,-1):
    value = ""
    for j in range(len(input)-1):
        value += input[j][i]
    if value != ' '*(len(input)-1):
        problems[-1].append(int(value))
    else:
        problems.append([])

total = 0
for i, problem in enumerate(problems):
    if args[i] == "*":
        answer = functools.reduce(lambda a, b: a * b, problem)
    else:
        answer = functools.reduce(lambda a, b: a + b, problem)
    total += answer

print(total)