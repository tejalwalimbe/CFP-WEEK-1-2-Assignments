#Flip coin program
import random
probability = 0
head = 0
tail = 0
a = int(input(" Enter number of times to flip coin "))
while probability!=a:
    b=random.randint(1,10) 
    print(b)
    if b<5:
        tail=tail+1
        probability=probability+1
    else:
        head=head+1
        probability=probability+1
print ("head win",(head/a*100))
print ("tail win",(tail/a*100))



                