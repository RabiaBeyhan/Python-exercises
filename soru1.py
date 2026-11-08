sayı=int(input("bir sayı söyle: "))
a=sayı
while(a>=0):
    print(a)
    a=a-1
print("Ateşle!")
##############
num=int(input("bir sayı girin: "))
sum=0
for number in range(0,num+1):
    sum+=number
print(sum)
############
mylist=[]
for i in range(1,10):
    for j in range(1,10):
        mylist.append(i*j)
    print(mylist)
    mylist.clear()