MarksList = []
for i in range(3):
    S = int(input("Enter the Marks for the Subjects: "))
    MarksList.append(S)
    for Marks in MarksList:
        if Marks >= 35:
            Pass = 1
        else:
            Pass = 0
if Pass == 1:
    print("Promoted")
else:
    print("Not Promoted")
