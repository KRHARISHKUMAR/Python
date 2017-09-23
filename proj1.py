#sales report
#read the file
file=open("C:\\Users\\Raceclass64\\Desktop\\harish\\proj1.txt")
#read the first line which contains header
header=file.readline()[0:-1]
headercoloums=header.split(",")
print(headercoloums)
#process other elements of the file
data = file.readlines()
file.close()
#prase the data
data1=[]
for element in data:
    
    print(type(element))
    
#find the data
#generate the data
