import random
import json

days = {}
outer = {}
for j in range(31):
    total = []
    for i in range(1,25):
        if 6 < i <= 9 or 14 < i <= 18:
            cold = random.randint(1, 2) + random.random()
            hot = random.randint(1, 5) + random.random()
        elif 18 < i <= 21:
            cold = random.randint(1, 2) + random.random()
            hot = random.randint(3, 9) + random.random()
        else:
            cold = random.randint(0, 1) + random.random()
            hot = random.randint(0, 1) + random.random()
        total_val = hot + cold
        if i < 10:
            strhour = "0" + str(i)
        else:
            strhour = i
        df = {'hour': "{}:00".format(strhour), 'cold': cold, 'hot': hot, 'total': total_val}
        total.append(df)
    outer[j] = total

days["03"] = outer

outer = {}
for j in range(6):
    total = []
    for i in range(1,25):
        if 6 < i <= 9 or 14 < i <= 18:
            cold = random.randint(1, 2) + random.random()
            hot = random.randint(1, 5) + random.random()
        elif 18 < i <= 21:
            cold = random.randint(1, 2) + random.random()
            hot = random.randint(3, 9) + random.random()
        else:
            cold = random.randint(0, 1) + random.random()
            hot = random.randint(0, 1) + random.random()
        total_val = hot + cold
        if i < 10:
            strhour = "0" + str(i)
        else:
            strhour = i
        df = {'hour': "{}:00".format(strhour), 'cold': cold, 'hot': hot, 'total': total_val}
        total.append(df)
    outer[j] = total
days["04"] = outer

with open('data.json', 'w') as outfile:
    json.dump(days, outfile)
