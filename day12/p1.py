import requests
from shape import Shape
SESSION_COOKIE = "53616c7465645f5f00eb92e40c3e8203648e23ee072ce796e6eb04a8d61ee84aa95c898be3d3a6f0fe29ca362d6f9dcfbaf99c873f0631df63f6f39d4096e489"
response = requests.get("https://adventofcode.com/2025/day/12/input", cookies = {'session': SESSION_COOKIE})

if response.status_code == 200:
    input = response.text
else:
    print(f"Error: {response.status_code}")

input = input.splitlines()

#create shapes
shapes = []
i_input = 0
while(len(input[i_input]) <= 2 or input[i_input][2] != "x"):
    if input[i_input][1] == ":":
        shapes.append(Shape(i_input, input[i_input+1:i_input+4]))
        i_input += 5
    else:
        i_input += 1

puzzles = []
#create puzzles
for i in range(i_input, len(input)):
    line = input[i]
    grid, shapes_needed = line.split(":")
    grid = tuple(map(lambda x: int(x), grid.split("x")))
    shapes_needed = list(map(lambda x: int(x), shapes_needed.split()))
    puzzles.append((grid, shapes_needed))

low_bound = 0
high_bound = 0
for puzzle in puzzles:
    grid, shapes_needed = puzzle
    #find highest bound of true answer: What if each square in the grid was filled up with a shape?
    max_size = sum(shapes_needed)*9
    min_size = 0
    area = grid[0]*grid[1]
    #find lowest bound of true answer: What if no shapes overlapped squares, so each shape needed 9 spots?
    for i, shape_num in enumerate(shapes_needed):
        min_size += shapes[i].size * shape_num
    if  area >= max_size:
        low_bound += 1
    if  area >= min_size:
        high_bound += 1

#wow what a surprise theyre the same number
print(f"Low bound: {low_bound}")
print(f"High bound: {high_bound}")






