# 1st Answer
for num in range(2000,3200):
    if(num%5!=0 and num%7==0):
        print(num,end=",")

#2nd answer

first=input("enter first name : ")
last=input("enter last name : ")

print(last[::-1]+" "+first[::-1])


#3rd answer

diameter=12
r=diameter/2
print("Volume of sphere = ",((4/3)*3.12*pow(r,3)))