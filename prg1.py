
a=list(map(int,input().strip().split()))
print(a)

def remove_dup():
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    print(b)

remove_dup()

c=[x**2 for x in range(int(input())) if x%2==0]

print(c)

c.reverse()

print(c)