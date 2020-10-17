n = int(input("Enter N value: "))
a = 0
b = 1
SumOFTerms = 1
for i in range(2, n):
    c = a + b
    a = b
    b = c
    SumOFTerms = SumOFTerms + c
print(SumOFTerms)
