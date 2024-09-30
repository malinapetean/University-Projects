# Solve the problem from the first set here
#For a given natural number n find the minimal natural
#number m formed with the same digits. (e.g. n=3658, m=3568)
def split(l,nr):
    while (nr):
        l[int(nr%10)]+=1
        nr=nr//10

def nrmin(l,ct):
    nrmin=0
    for i in range(0,10):
        if(i==0 and l[i]!=0):
            ct=l[i]
        elif(l[i]!=0):
            while(l[i]):
                nrmin=nrmin*10+i
                l[i]-=1
            while(ct!=0):
                nrmin*=10
                ct=ct-1
    return nrmin
l=[0,0,0,0,0,0,0,0,0,0]
print("write a number: ")
nr=input()
nr=int(nr)
print("the minimum number formed with the same digits of",nr, "is:")
split(l,nr)
nr=nrmin(l,0)
print(nr)
        
            
