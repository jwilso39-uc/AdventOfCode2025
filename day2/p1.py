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
        done = False
        if len(str_id) % 2 == 1:
            continue
        else:
            lasthalf = str_id[len(str_id)//2:]
            firsthalf = str_id[:len(str_id)//2]
            if lasthalf == firsthalf:
                id_sum += id
                print(id)
        #Forgot what the problem actually asked initially but it might be p2
        """
        for i, char  in enumerate(str_id):
            #each letter has (i+1)//2 checks
            for j in range((i+1)//2):
                cur_str = str_id[i-j:i+1]
                prev_str = str_id[i-(2*j + 1):i-j]
                if cur_str == prev_str:
                    id_sum += int(str_id)
                    done = True
                    break
            if done:
                print(str_id)
                break
        """

print(id_sum)





