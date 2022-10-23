# Write a python program to check if all items in the tuple are the same.
t1=(10,20,30,40,50,10)
for e in t1:
 a=t1.count(e)
 b=len(t1)
 if a>1:
    print(e,'repeted for',a,'times')
 if a==1:
    print("item is not same")
 if a==b:
    print("All item is same")   
       
    


    