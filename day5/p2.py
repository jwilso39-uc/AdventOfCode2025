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
i = 0
"""while i < len(intervals)-1:
    if intervals[i][0] == intervals[i+1][0] and intervals[i][1] == -intervals[i+1][1]:
        intervals.pop(i)
        intervals.pop(i)
        i -= 1
    i += 1"""

fresh = 0
fresh_ids = 0
pass_next = False

#find fresh ids - assume that itervals input is well-formatted
for i, interval in enumerate(intervals):
    if pass_next:
        pass_next = False
        continue
    if fresh == 0:
        start = interval[0]
    fresh += interval[1]
    if fresh == 0:
        if i < len(intervals)-1 and interval[0] == intervals[i+1][0]:
            pass_next = True
            fresh += 1
            continue
        end = interval[0]
        fresh_ids += (end - start + 1)

print(fresh_ids)
