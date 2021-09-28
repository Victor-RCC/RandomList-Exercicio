import random

randomList = []
newRandomList = []
d = 50
major = 0

for i in range(d):
    randomList.append(random.randint(0, d))
    major = randomList[0]
    if randomList[i] > major:
        major = i
        newRandomList.append(major)

print(newRandomList)