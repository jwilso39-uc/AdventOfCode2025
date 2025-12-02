import requests
SESSION_COOKIE = "53616c7465645f5f00eb92e40c3e8203648e23ee072ce796e6eb04a8d61ee84aa95c898be3d3a6f0fe29ca362d6f9dcfbaf99c873f0631df63f6f39d4096e489"
response = requests.get("https://adventofcode.com/2025/day/1/input", cookies = {'session': SESSION_COOKIE})

if response.status_code == 200:
    input = response.text
else:
    print(f"Error: {response.status_code}")

data = input.splitlines()

dial = 50
password = 0
for turn in data:
    print(f"Dial: {dial}, pw: {password}")
    direction = turn[0]
    clicks = int(turn[1:])
    if direction == 'R':
        print(f"Turning {direction} for {clicks} clicks. Upping password by {(dial + clicks)//100}")
        password += (dial + clicks)//100
        dial = (dial + clicks) % 100
    else:
        print(f"Turning {direction} for {clicks} clicks. Upping password by {abs((dial - clicks))//100}")
        print(f"Adding one more: {dial - clicks <= 0 and dial != 0}")
        if dial - clicks <= 0 and dial != 0:
            password += 1
        password += abs((dial - clicks))//100
        dial = (dial - clicks) % 100

print(f"The really true password is: {password}")