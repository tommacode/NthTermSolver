inputstr = str(input('Enter an nth term sequence: '))
sequence = inputstr.split(',')
for i in range(0,len(sequence)):
    sequence[i] = int(sequence[i])
firstDifference = [int]*int(len(sequence)-1)
secondDifference = [int]*int(len(sequence)-2)

for i in range(0,len(sequence)-1):
    firstDifference[i] = sequence[i+1] - sequence[i]

for i in range(0,len(firstDifference)-1):
    secondDifference[i] = firstDifference[i+1] - firstDifference[i]
print(sequence)
def getA():
    a = secondDifference[i]
    a = a/2
    return a
a = getA()
def getB(a):
    b=firstDifference[0]
    b=b-3*a
    return b
b = getB(a)
def getC(a,b):
    c=sequence[0]
    c=c-b
    c=c-a
    return c
c = getC(a,b)

print(str(int(a)) + 'n**2 + ' + str(int(b)) +'n + ' + str(int(c)))
