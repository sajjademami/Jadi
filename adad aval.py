inp=[]
maghsomha=[]
khoroji=[]
a=0
x=[]

###############################################
for i in range(1):
    inp.append(int(input()))
################################################
def isprime(number):
    count=0
    for num in range(1, number - 1):
        if number % num == 0:
            count += 1
    return x.append(number), x.append(count)
###############################################

def tedad(adad):
    for maghsom in range(1, adad - 1):
        if adad % maghsom== 0:
            maghsomha.append(maghsom)
    return maghsomha
###############################################
for elements in inp:
    for w in tedad(elements):
        print(isprime(w))

print(tedad(elements))








#print(x[0],x[1])
