# UserInput Program 
#take input from user
name = input ("Enter Username:")
#variable declaration
str1 = " Hello "
str2 = "<< UserName >>"
str3 = " How Are U?? "

str4 = str1 +str2 +str3
print ("Initial string ="+str4) 
print ("Enter the name to replace\n")
if (len(name)>=3):
    str4 = str1 +name +str3
    print ("The replaced name is = "+str4)
else:
    print ("Enter name having more than 3 characters")
