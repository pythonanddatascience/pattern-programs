# pattern-programs

### here you can see some of the pattern in this pattern.py file 

Every forloop is one pattern 


for i in range(n):
    for j in range(i+1):
        print(j+1, end  = ' ')
    print()

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

#### please observe the o=above code and below code  i added only two lines extra  

'''

for j in range(n-i-1):
    print(" ", end = " ")
''' 

###### above lines i added 

for i in range(n):
    for j in range(n-i-1):
        print(" ", end =' ')
    for j in range(i+1):
        print(j+1, end  = ' ')
    print()


        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 

#### please observe the above and below code , they look same i just changed a small thing that is removed space at the end=""
for i in range(n):
    for j in range(n-i-1):
        print(" ", end ="") # here i  just removed spaced at the (end ="") if u give space above pattern will comes 
    for j in range(i+1):
        print(j+1, end  = ' ')
    print()
    
     1 
   1 2 
  1 2 3 
 1 2 3 4 
1 2 3 4 5 
   
    
