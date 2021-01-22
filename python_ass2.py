# 1st Answer

for i in range(1,6):
    for j in range(0,i):
        print("*",end=" ")
    print()
for i in reversed(range(5)):
    for j in range(0,i):
        print("*",end=" ")
    print()

# 2nd answer

inp=input("enter any input : ")
print(inp[::-1])

