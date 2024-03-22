myfile=open("Sample_for_file_open.txt",'r')

#data=myfile.read(10)
#print(data)
#print(myfile.read(20))

data=myfile.readlines(3)
print(data)
print(myfile.read(20))
