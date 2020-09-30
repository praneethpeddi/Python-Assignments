n = int(input('Enter n value: '))
elements = []
Outputs = []
for i in range(n):
    num = int(input('Enter a number: '))
    elements.append(num)
print(elements)
for i in elements:
    if i not in Outputs:
        Outputs.append(i)
print(Outputs)