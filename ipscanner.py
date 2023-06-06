import os
import csv

hostname=[]
with open('iplist.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        hostname.append((row[0]))
#print(hostname)
online=0
offlinelist=[]
offline=0
for i in range(len(hostname)):
    response = os.system("ping -n 1 " + hostname[i] + " > nul") #and then check the response...
    if response == 0:
        print ('🟩',hostname[i])
        online+=1
    else:
        print ('🟥',hostname[i])
        offline+=1
        offlinelist.append(hostname[i])

print('Total', len(hostname))        
print('Online: ', online)
print('Offline', offline)
print('Offline List: ',offlinelist)

input("press ENTER")