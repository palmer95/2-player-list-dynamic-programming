def main():

    A = [49, 100, 61, 36, 16, 43, 52, 7, 76, 11]
    #A = [3, 9, 1, 2, 4, 6]

    prev = initializeTable(A)
    j = 3

    while len(prev) > 1:
        prev = minMax(j, prev, A)
        j += 2

    print(prev)

def minMax(j, prev, A):

    current = []

    for i in range(len(prev) - 2):
        choice = max(min(prev[i+2], prev[i+1]) + A[i], min(prev[i+1], prev[i]) + A[j])
        #print (choice)
        current.append(choice)
        j += 1

    return current

def initializeTable(Scores):

    init = []
    for i in range(len(Scores)-1):
        init.append(max(Scores[i],Scores[i+1]))

    return init

main()