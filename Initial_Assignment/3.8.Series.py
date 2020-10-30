n = int(input('Enter a number: '))
fact1 = 1
fact2 = 1
fact1Lis1 = []
fact2Lis2 = []
for i in range(2, n + 1):
    fact1 *= i
    fact1Lis1.append(fact1)
print(fact1Lis1)
for j in range(1, n):
    fact2 *= j
    fact2Lis2.append(fact2)
print(fact2Lis2)
res = [i / j for i, j in zip(fact1Lis1, fact2Lis2)]
print(sum(res))
