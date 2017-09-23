#read a file and print word stats
file1=open("C:\\Users\\Raceclass64\\Desktop\\harish\\sample.txt")
data = file1.readlines()
print(data)
file1.close()

#strip each sentence of new line
data1 = []
for element in data:
    print(element)
    if(element[-1]=='\n'):
        data1.append(element[0:-1])
    else:
        data1.append(element)
print(element)

