def UseN():
    nthTerm = input('Input an nth term: ')
    repeats = int(input('How many times would you like this sequence to complete: '))
    for n in range(1,repeats):
        print(eval(nthTerm),end=",")

def GetN():
    inputstr = str(input('Enter an nth term sequence: '))
    sequence = inputstr.split(',')
    for i in range(0, len(sequence)):
        sequence[i] = int(sequence[i])
    firstDifference = [int] * int(len(sequence) - 1)
    
    for i in range(0, len(sequence) - 1):
        firstDifference[i] = sequence[i + 1] - sequence[i]
    
    
    def QuadraticSeq(firstDifference, sequence):
        secondDifference = [int] * int(len(sequence) - 2)
        for i in range(0, len(firstDifference) - 1):
            secondDifference[i] = firstDifference[i + 1] - firstDifference[i]
    
        def getA():
            a = secondDifference[i]
            a = a / 2
            return a
    
        a = getA()
    
        def getB(a):
            b = firstDifference[0]
            b = b - 3 * a
            return b
    
        b = getB(a)
    
        def getC(a, b):
            c = sequence[0]
            c = c - b
            c = c - a
            return c
    
        c = getC(a, b)
    
        print(str(int(a)) + 'n**2 + ' + str(int(b)) + 'n + ' + str(int(c)))
    
    
    def NonQuadratic(firstDifference, sequence):
    
        print(
            str(firstDifference[0]) + 'n + ' + str(sequence[1] -
                                                   (firstDifference[1] * 2)))
    
    
    if firstDifference[0] == firstDifference[1]:
        #not Quadratic
        NonQuadratic(firstDifference, sequence)
    else:
        QuadraticSeq(firstDifference, sequence)


if input('Welcome To the Nth Term machine! \n type 1 for using an nth term to make a sequence or type 2 for finding an nth term from a sequence: ') == '1':
    UseN()
    input('Done')
if input('Welcome To the Nth Term machine! \n type 1 for using an nth term to make a sequence or type 2 for finding an nth term from a sequence: ') == '2':
    GetN()
    input('Done')

    