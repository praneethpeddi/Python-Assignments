n = int(input('Enter a number: '))
fact = 1
SumOfSeries = 0
for i in range(1, n+1):
    fact *= i
    SumOfSeries = SumOfSeries + fact
print(SumOfSeries)
