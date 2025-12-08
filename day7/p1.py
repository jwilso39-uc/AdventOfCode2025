import requests
SESSION_COOKIE = "53616c7465645f5f00eb92e40c3e8203648e23ee072ce796e6eb04a8d61ee84aa95c898be3d3a6f0fe29ca362d6f9dcfbaf99c873f0631df63f6f39d4096e489"
response = requests.get("https://adventofcode.com/2025/day/7/input", cookies = {'session': SESSION_COOKIE})

if response.status_code == 200:
    input = response.text
else:
    print(f"Error: {response.status_code}")

input = input.splitlines()


beams = set()
beams.add(input[0].find('S'))

splits = 0

for line in input[1:]:
    next_line_beams = beams.copy()
    for beam in beams:
        if line[beam] == '^':
            next_line_beams.remove(beam)
            next_line_beams.add(beam+1)
            next_line_beams.add(beam-1)
            splits+=1
    beams = next_line_beams.copy()

print(splits)

