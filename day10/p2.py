import requests
import cvxpy as cp
import functools
SESSION_COOKIE = "53616c7465645f5f00eb92e40c3e8203648e23ee072ce796e6eb04a8d61ee84aa95c898be3d3a6f0fe29ca362d6f9dcfbaf99c873f0631df63f6f39d4096e489"
response = requests.get("https://adventofcode.com/2025/day/10/input", cookies = {'session': SESSION_COOKIE})

if response.status_code == 200:
    input = response.text
else:
    print(f"Error: {response.status_code}")

def format_lights(char):
    if char == "#":
        return True
    else:
        return False

def format_input(machine):
    lights, rest = machine.split("]")
    lights = lights[1:]
    lights = list(map(format_lights,lights))
    buttons_str, joltage = rest.split("{")
    buttons_str = buttons_str.replace(" (","")
    buttons_str = buttons_str.replace(" ","")
    buttons_str = buttons_str.split(")")
    buttons_str = buttons_str[:-1]
    buttons = []
    for button in buttons_str:
        buttons.append(tuple(map(lambda x: int(x),button.split(","))))
    joltage = joltage.replace("}","")
    joltage = list(map(lambda x: int(x), joltage.split(",")))
    return lights, buttons, joltage

input = input.splitlines()

total = 0
for machine in input:
    lights, buttons, joltage = format_input(machine)
    #find which buttons hit what lights
    button_lights = [[] for _ in range(len(lights))]
    for i, button in enumerate(buttons):
        for j in range(len(button)):
            button_lights[button[j]].append(i)

    #create variables
    lights_var = cp.Variable(len(lights), integer = True)
    buttons_var = cp.Variable(len(buttons), integer = True)
    #lights should be either even or odd
    constraints = []
    #add light constraints
    for i in range(len(lights)):
        constraints.append(lights_var[i] == joltage[i])
        toggles = 0
        for j in button_lights[i]:
            toggles += buttons_var[j]
        constraints.append(lights_var[i] == toggles)
    #now minimize the number of buttons that are on
    obj_func = 0
    for i, button in enumerate(buttons_var): # type: ignore
        constraints.append(buttons_var[i]>=0)
        obj_func += button
    obj = cp.Minimize(obj_func)
    prob = cp.Problem(obj, constraints)
    prob.solve()
    #print("status:", prob.status)
    #print("optimal value", prob.value)
    total += prob.value # type: ignore
print(total)





    
    


