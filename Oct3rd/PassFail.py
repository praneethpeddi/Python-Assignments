MarksList = []
for i in range(3):
    S = int(input("Enter the Marks for the Subjects: "))
    MarksList.append(S)
    fail = 0
for Marks in MarksList:
    if Marks < 35:
        fail = 1
if fail == 0:
    print("Promoted")
else:
    print("Not Promoted")
