n = int(input("Enter the number of rows you need : "))

for i in range(n):
    for j in range(i+1):
        print(j+1, end  = ' ')
    print()


for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, end =' ')
    print()


for i in range(n):
    for j in range(i, -1, -1):
        print(j+1, end = ' ')
    print()

for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end = " ")
    print()


for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end =" ")
    print()


for i in range(n):
    for j in range(i, -1, -1):
        print(i+1, end = ' ')
    print()


for i in range(n):
    for j in range(i+1):
        print(i+1, end = ' ')
    print()


for i in range(n):
    for j in range(i+1):
        print(n-i, end = " ")
    print()

for i in range(1,n+1):
    for j in range(i):
        print(n+1-i, end = ' ')
    print()

for i in range(1,n+1):
    for j in range(i):
        print(n-j, end =" ")
    print()

for i in range(n):
    for j in range(i+1):
        print(n-j, end = ' ')
    print()

for i in range(n):
    for j in range(i, -1,-1):
        print(n-j, end = ' ')
    print()

for i in range(1,n+1):
    for j in range(i,0,-1):
        print(n+1-j, end = " ")
    print()





###########################################


for i in range(n):
    for j in range(n-i-1):
        print(" ", end =' ')
    for j in range(i+1):
        print(j+1, end  = ' ')
    print()

for i in range(n):
    for j in range(n-i-1):
        print(" ",end = " ")
    for j in range(i, -1, -1):
        print(j+1, end = ' ')
    print()



for i in range(n):
    for j in range(n-i-1):
        print(" ", end =" ")
    for j in range(i, -1, -1):
        print(i+1, end = ' ')
    print()

for i in range(n):
    for j in range(n-i-1):
        print(" ", end= " ")
    for j in range(i+1):
        print(n-i, end = " ")
    print()

for i in range(n):
    for j in range(n-i-1):
        print(" ", end = " ")
    for j in range(i+1):
        print(n-j, end = ' ')
    print()


for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(i, -1,-1):
        print(n-j, end = ' ')
    print()
'''

for j in range(n-i-1):
    print(" ", end = " ")
'''

for i in range(n):
    for j in range(n-i-1):
        print(" ", end ="")
    for j in range(i+1):
        print(j+1, end  = ' ')
    print()

for i in range(n):
    for j in range(n-i-1):
        print(" ",end = "")
    for j in range(i, -1, -1):
        print(j+1, end = ' ')
    print()


for i in range(n):
    for j in range(n-i-1):
        print(" ", end ="")
    for j in range(i, -1, -1):
        print(i+1, end = ' ')
    print()

for i in range(n):
    for j in range(n-i-1):
        print(" ", end= "")
    for j in range(i+1):
        print(n-i, end = " ")
    print()

for i in range(n):
    for j in range(n-i-1):
        print(" ", end = "")
    for j in range(i+1):
        print(n-j, end = ' ')
    print()


for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i, -1,-1):
        print(n-j, end = ' ')
    print()



# reverse pyramid

for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ", end ="")
    for j in range(i+1):
        print(j+1, end  = ' ')
    print()

for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ",end = "")
    for j in range(i, -1, -1):
        print(j+1, end = ' ')
    print()


for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ", end ="")
    for j in range(i, -1, -1):
        print(i+1, end = ' ')
    print()

for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ", end= "")
    for j in range(i+1):
        print(n-i, end = " ")
    print()

for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ", end = "")
    for j in range(i+1):
        print(n-j, end = ' ')
    print()


for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i, -1,-1):
        print(n-j, end = ' ')
    print()


n = 8
num = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(format(num,("<3")),end = " ")
        num = num+1
    print()

n = 6

for i in range(n):
    val = i+1
    dec = n-1
    for j in range(i+1):
        print(format(val, "<2"), end = " ")
        val = val+dec
        dec = dec -1

    print()

num =  6

for i in range(1, num+1):
    for j in  range(1,num-i+1):
        print(end =" ")
    for j in range(i,0,-1):
        print(j, end ="")
    for j in range(2,i+1):
        print(j, end="")

    print()



#..........................................................




n = int(input('enter the number of rows : '))
for i in range(n):
    val = i+1
    dec = n-1
    for j in range(i+1):
        print(val, end=" ")
        val = val+dec
        dec = dec-1
    print()


n=4
num =1
for i in range(1,n+1):
    for j in range(1, n-i+1):
        print(" ", end = " ")
    for j in range(1,i+1):
        print(num, end=" ")
        num = num + 1
    print()








string = 'python'
for i in range(1, len(string)+1):
    for j in range(i):
        print(string[j], end=" ")
    print()


for i in range(1, len(string)+1):
    for j in range(1, len(string)-i+1):
        print(" ", end=" ")
    for j in range(i):
        print(string[j], end=" ")
    print()

for i in range(1, len(string)+1):
    for j in range(1, len(string)-i+1):
        print(end=" ")
    for j in range(i):
        print(string[j], end=" ")
    print()



for i in range(len(string),0,-1):
    for j in range(1, len(string)-i+1):
        print(" ",end=" ")
    for j in range(0,i):
        print(string[j], end = " ")
    print()



for i in range(len(string),0,-1):
    for j in range(1, len(string)-i+1):
        print(" ",end="")
    for j in range(0,i):
        print(string[j], end = " ")
    print()

for i in range(len(string),0,-1):
    for j in range(0,i):
        print(string[j], end = " ")
    print()


for i in range(0, len(string)):
    for j in range(0,i+1,):
        print(string[i], end=" ")
    print()



for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j, end =' ')
    print()

for i in range(n,0,-1):
    for j in range(1, n-i+1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j, end =' ')
    print()

for i in range(n,0,-1):
    for j in range(1, n-i+1):
        print(" ",end="")
    for j in range(i,0,-1):
        print(j, end =' ')
    print()


for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j, end = " ")
    print()

for i in range(n,0,-1):
    for j in range(1, n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j, end = " ")
    print()

for i in range(n,0,-1):
    for j in range(1, n-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print(j, end = " ")
    print()


for i in range(n,0,-1):
    for j in range(i, 0, -1):
        print(i, end = ' ')
    print()

for i in range(n,0,-1):
    for j in range(1, n-i+1):
        print(" ",end=" ")
    for j in range(i, 0, -1):
        print(i, end = ' ')
    print()

for i in range(n,0,-1):
    for j in range(1, n-i+1):
        print(" ",end="")
    for j in range(i, 0, -1):
        print(i, end = ' ')
    print()


n=5
for i in range(n-1,-1,-1):
    for j in range(i,-1,-1):
        print(n-i, end = " ")
    print()

for i in range(n-1,-1,-1):
    for j in range(1,n-i+1):
        print(" ", end=" ")
    for j in range(i,-1,-1):
        print(n-i, end = " ")
    print()

for i in range(n-1,-1,-1):
    for j in range(1,n-i+1):
        print(" ", end="")
    for j in range(i,-1,-1):
        print(n-i, end = " ")
    print()
