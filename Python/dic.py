
import string
alphabetList=list(string.ascii_lowercase[:26])
numList=list(range(1,27))

mydict = dict()
for i in numList:
    mydict[alphabetList[i-1]]=i
print("{}\n{}\n".format("dic: ",mydict)) 
#get count
print("{}\n{}\n".format("get len: ",len(mydict))) 

#delete h
del mydict["h"]
print("{}\n{}\n".format("delet [h]: ",mydict)) 

#get value >5
mydict["i"]=0
print("{}\n{}\n".format("value >5: ",{k: v for k, v in mydict.items() if v > 5 })) 

#if exist key[h]
if 'h' in mydict:
    print ("exist\n")
else:
    print ("cannot found key[h]\n")

#if exist value 9
if 9 in mydict:
    print ("exist\n")
else:
    print ("cannot found value 9\n")

#print key
print(mydict.keys())

#pring value
print(mydict.values())

#clear dict
mydict.clear()
print(mydict)
