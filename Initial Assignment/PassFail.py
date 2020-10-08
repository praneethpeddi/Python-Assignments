MarksList = []
for i in range(3):
    S = int(input("Enter the Marks for the Subjects: "))
    MarksList.append(S)
    Status = True
for Marks in MarksList:
    if Marks < 35:
        Status = False
if Status:
    print("Promoted")
else:
    print("Not Promoted")