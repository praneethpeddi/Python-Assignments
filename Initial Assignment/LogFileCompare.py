StrToSearch = 'warning'
with open(r'C:\Users\user\Desktop\Python Training\Lectures\Day 1_Oct 3rd\OneDrive-2020-10-02\1log.txt', 'r') as f1:
    File1Data = f1.read().split('\n')
    count1 = 0
    for i in File1Data:
        if StrToSearch in i:
            count1 = count1 + 1
    # print(StrToSearch + ' ' + 'is displayed for' + ' ' + str(count1) + ' ' + 'times')

with open(r'C:\Users\user\Desktop\Python Training\Lectures\Day 1_Oct 3rd\OneDrive-2020-10-02\2log.txt', 'r') as f2:
    File2Data = f2.read().split('\n')
    count2 = 0
    for i in File2Data:
        if StrToSearch in i:
            count2 = count2 + 1
    # print(StrToSearch + ' ' + 'is displayed for' + ' ' + str(count2) + ' ' + 'times')

if count1 < count2:
    print("*** New Warnings are introduced in the current build, can't be promoted\n" 
          '*** Old     Warning count 1log.txt:' + str(count1) + '\n' +
          '*** Current Warning count 2log.txt:' + str(count2) + '\n' +
          "Build CAN'T be promoted")
else:
    print('*** Old     Warning count 1log.txt:' + str(count1) + '\n' +
          '*** Current Warning count 2log.txt:' + str(count2) + '\n' +
          'Build promoted')
