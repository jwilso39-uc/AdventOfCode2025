import requests
SESSION_COOKIE = "53616c7465645f5f00eb92e40c3e8203648e23ee072ce796e6eb04a8d61ee84aa95c898be3d3a6f0fe29ca362d6f9dcfbaf99c873f0631df63f6f39d4096e489"
response = requests.get("https://adventofcode.com/2025/day/2/input", cookies = {'session': SESSION_COOKIE})

if response.status_code == 200:
    input = response.text
else:
    print(f"Error: {response.status_code}")

id_sum = 0

intervals = input.split(',')
for interval in intervals:
    #get ids to check
    endpoints = interval.split('-')
    start = int(endpoints[0])
    end = int(endpoints[1])

    for id in range(start, end + 1):
        str_id = str(id)
        valid_id = True
        for i in range(1,len(str_id)):
            if len(str_id) % i == 0:
                prev_seq = str_id[0:i]
                for j in range(1,len(str_id)//i):
                    cur_seq = str_id[j*i:(j*i)+i]
                    if cur_seq != prev_seq:
                        break
                    #print(f"i={i}, j={j}, prev = {prev_seq}, cur_seq={cur_seq}, id={id}")
                    if j == len(str_id)//i - 1:
                        valid_id = False
                        #print(id)
                        id_sum += id
                if not valid_id:
                    break

print(id_sum)