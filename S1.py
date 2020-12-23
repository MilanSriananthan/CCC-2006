def switch(word):
    answer = []
    for i in word:
        if i == i.upper():
            answer.append(2)
        else:
            answer.append(1)
    return answer
def attribute(value):
    if value.upper() == value:
        return 2
    if value.lower() == value:
        return 1
    return 0

def result(val1, val2):
    if val1 == val2:
        return val1
    if val1 == 2 or val2 == 2:
        return 2
    return 0
mother = input()
father = input()
mcode = []
fcode = []
for i in range(5):
    mcode.append(mother[i*2:(i+1)*2])
    fcode.append(father[i*2:(i+1)*2])

mother = []
father = []
combined = []
for i in range(5):
    save = attribute(mcode[i])
    mother.append(save)
    save = attribute(fcode[i])
    father.append(save)

for i in range(5):
    save = result(mother[i], father[i])
    combined.append(save)

numkids = int(input())

for i in range(numkids):
    w = 0
    kid = input()
    kid = switch(kid)
    for x in range(5):
        if kid[x] != combined[x] and combined[x] != 0:
            w = 1
            print("Not their baby!")
            break
    if w == 0:
        print("Possible baby.")



