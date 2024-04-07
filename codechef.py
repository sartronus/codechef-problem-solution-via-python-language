#codechef number mirror solution
N=int(input())
if 0<=N<=10*10*10*10*10 :
    print(N)
else:
    print("error")
#codechef chef and instant noodle problem
x,y= map(int,input().split())
ans=x*y
print(ans)
#codechef chef and brain speed problem
limit,current=map (int,input().split())

if current > limit :
    print("yes")
else:
    print("no")
#codechef alice and marks problem
x,y=[int(i) for i in input().split()]
if x>=2*y:
    print("yes")
else:
    print("no")
#codechef onefull pair problem
a,b=[int(i) for i in input().split()]
if a+b+(a*b)==111:
    print("yes")

else:
    print("no")
#codechef add two numbers problem
t=int(input())
for i in range(t):
    (a,b)=map(int,input().split())
    ans=a+b
    print(ans)
#codechef good turn problem
TC=int(input())
for T in range (TC):
    x,y=map(int,input().split())
    if (x+y>6):
        print("yes")
    else:
        print("no")
#codechef water consumption problem
t = int(input())
for i in range(0,t):
    x =  int(input())
    if x >= 2000:
        print("yes")
    else:
        print("no")
#codechef age limit problem
for _ in range(int(input())):
    a=list(map(int,input().split()))
    if a[2] >= a[0] and a[2] < a[1]:
        print('YES')
    else:
        print('NO')
#codechef biryani problem
t = int(input())
for i in range(t):
    X,Y= map(int,input().split())
    m=X*Y
    print(m)
#codechef burger problem
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a<=b:
        print(a)
    else:
        print(b)
#codechef height problem
t=int(input())
for i in range(t):
    A,B=map(int,input().split())
    if A>B:
        print('A')
    else:
        print('B')