import requests
SESSION_COOKIE = "53616c7465645f5f00eb92e40c3e8203648e23ee072ce796e6eb04a8d61ee84aa95c898be3d3a6f0fe29ca362d6f9dcfbaf99c873f0631df63f6f39d4096e489"
response = requests.get("https://adventofcode.com/2025/day/5/input", cookies = {'session': SESSION_COOKIE})

if response.status_code == 200:
    input = response.text
else:
    print(f"Error: {response.status_code}")

input = input.splitlines()

#interpret ranges
intervals = []
for i, line in enumerate(input):
    if line=="":
        begin_ids = i+1
        break
    else:
        start, stop = line.split("-")
        intervals.append((int(start), 1))
        intervals.append((int(stop), -1))
    
intervals.sort(key = lambda x: x[0])
fresh = 0

#calculate fresh ingredients
for i in range(begin_ids, len(input)):
    j = 0
    inside = 0
    #cant do binary search because you need to know how many intervals you're in 
    while j < len(intervals) and int(input[i]) > intervals[j][0]:
        inside += intervals[j][1]
        j += 1
    if inside > 0:
        fresh += 1

print(fresh)