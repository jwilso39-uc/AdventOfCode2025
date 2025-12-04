import requests
SESSION_COOKIE = "53616c7465645f5f00eb92e40c3e8203648e23ee072ce796e6eb04a8d61ee84aa95c898be3d3a6f0fe29ca362d6f9dcfbaf99c873f0631df63f6f39d4096e489"
response = requests.get("https://adventofcode.com/2025/day/3/input", cookies = {'session': SESSION_COOKIE})

if response.status_code == 200:
    input = response.text
else:
    print(f"Error: {response.status_code}")

banks = input.splitlines()

turn_on = 12
joltage_sum = 0
#iterative solution
for bank in banks:
    jolt = [0 for _ in range(turn_on)]
    for i, char in enumerate(bank):
        joltage = int(char)
        for j in range(turn_on):
            if i+turn_on-j <= len(bank) and joltage > jolt[j]:
                jolt[j] = joltage
                for k in range(j+1,turn_on):
                    jolt[k] = 0
                break
    joltage_bank = ""
    for i in range(turn_on):
        joltage_bank = joltage_bank + str(jolt[i])
    joltage_bank = int(joltage_bank)
    print(joltage_bank)
    joltage_sum += joltage_bank

def get_index(jolt):
    min_val = 0
    for i, val in enumerate(jolt):
        if i == 0:
            continue
        if val>=min_val:
            min_val = val
            min_i = i
    return min_i-1

print(f"total = {joltage_sum}")

#DP-like solution - doesn't work right now, but I bet you could do it this way somehow
"""
joltage_sum = 0
for bank in banks:
    jolt = [int(bank[i]) for i in range(len(bank)-turn_on, len(bank))]
    for i in range(len(bank)-turn_on-1, -1, -1):
        joltage = int(bank[i])
        if joltage >= jolt[0]:
            jolt.insert(0, joltage)
            min_index = get_index(jolt)
            jolt.pop(min_index)
    joltage_bank = ""
    for i in range(turn_on):
        joltage_bank = joltage_bank + str(jolt[i])
    joltage_bank = int(joltage_bank)
    print(joltage_bank)
    joltage_sum += joltage_bank
    
print(joltage_sum)
"""