import requests
SESSION_COOKIE = "53616c7465645f5f00eb92e40c3e8203648e23ee072ce796e6eb04a8d61ee84aa95c898be3d3a6f0fe29ca362d6f9dcfbaf99c873f0631df63f6f39d4096e489"
response = requests.get("https://adventofcode.com/2025/day/3/input", cookies = {'session': SESSION_COOKIE})

if response.status_code == 200:
    input = response.text
else:
    print(f"Error: {response.status_code}")

banks = input.splitlines()

joltage_sum = 0

for bank in banks:
    jolt = [0,0]
    for i, char in enumerate(bank):
        joltage = int(char)
        if joltage > jolt[0] and (i+1) != len(bank):
            jolt[0] = joltage
            jolt[1] = int(bank[i+1])
        elif joltage > jolt[1]:
            jolt[1] = joltage
    joltage_bank = int(str(jolt[0])+str(jolt[1]))
    print(joltage_bank)
    joltage_sum += joltage_bank

print(f"total = {joltage_sum}")
        
