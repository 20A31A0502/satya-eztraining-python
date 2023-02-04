p1=(input("Enter the first person name:")).lower()
p2=(input("Enter the second person name:")).lower()
#if you give first and last time
#with space inbetween
p1=p1.replace(" ","")
p2=p2.replace(" ","")
print(p1)
print(p2)

for i in p1:
    for j in p2:
        if i==j:
            p1=p1.replace(i,"",1)
            p2=p2.replace(j,"",1)
            break
count=len(p1+p2)
print(count)
if count>0:
    list1=["Friends","Lovers","Affectionate","Marriage","Enemies","Sibling"]
    while len(list1)>1:
        c=count%len(list1)
        s_index=c-1
#slicing
        if s_index>=0:
            left=list1[:s_index]
            right=list1[s_index+1:]
            list1=right+left
        else:
            list1=list1[:len(list1)-1]
    print("Relationship:",list1[0])
else:
    print("Enter different names:")
