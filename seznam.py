n=int(input())
A=[]
for i in range(n):
    cislo=int(input())
    A.append(cislo)
#print(A)
m=int(input())
B=[]
for i in range(m):
    cislo=int(input())
    B.append(cislo)
#print(B)
dvojce=0
for x in A:
    for y in B:
        if x == y:
            dvojce+=1
print(dvojce)