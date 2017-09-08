import csv
import re 
import string

level1 =[]
level2 = []
data1 =[]
data2 = []
data3 =[]
data4 =[]
data5 = []
data6 = []
data7 = []
data8 = []
data9 = []
data10 = []


listname = raw_input ("Enter List Name:")
listname_accept = (listname) + '.csv'

with open('initial.csv') as f:
     reader = csv.reader(f,  delimiter = ',')
     i=0  
     for row in reader:
     	 if row == ['']:
     	 	          a=1
     	 else:
               myString = " ".join(row)

               data1 = myString.split(',',1)
               if(len(data1) == 1):
                  if(len(data3) == 0):
                     del data1
                  else:
                     data3[len(data3)-1] =  data3[len(data3)-1] + myString
                     
               elif (len(data1) == 2):  
                      if myString.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
                        data2.append(data1[0])
                        data3.append(data1[1])
                    # print data3
                      else:
                        data3[len(data3)-1] = data3[len(data3)-1] + myString
                    # data3[len(data3)-1] = data3[len(data3)-1] + data1

               else:
                    print "Invalid Chat Line"               
              # data2.append(data1[0])
              # data3.append(data1[1])
              # print data2[i]
              # print data3[i]
              # i=i+1
     for t in data2:
      #print t
      data4 = t.split()
      data5.append(data4[0])
      data6.append(data4[1])
     for s in data3:
      #print s
      data7 = s.split(':',1)
      data8.append(data7[0])
      data9.append(data7[1])

        
#print data4
# print data3
zip(data5,data6,data8,data9)

with open(listname_accept,'w') as cleaned:
     accept_writer=csv.writer(cleaned)
     accept_writer.writerows(zip(data5,data6,data8,data9))

 