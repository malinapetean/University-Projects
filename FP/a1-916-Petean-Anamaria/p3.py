# Solve the problem from the third set here
#Determine the n-th element of the sequence 1,2,3,2,5,2,3,7,2,3,2,5,...
#obtained from the sequence of natural numbers by replacing composed numbers
#with their prime divisors, without memorizing the elements of the sequence.
def prime_nr(nr):
    if(nr==0 or nr==1):
        return 0
    else:
        for i in range(2,nr):
            if(nr%i==0):
                return 0
    return 1

def nrpdiv(nr):
    ct=0
    for i in range(2,nr+1):
        if(nr%i==0 and prime_nr(i)==1):
            ct+=1
    return ct

def number_divisor(n):
    if(n == 1):
        return[1, 1]
    ct = 1
    i = 1
    number = 0
    k = 0
    while(ct<n):
        div = nrpdiv(i)
        if(ct + div < n):
            ct += div
            number = i + 1
            k = 0
        else:
            val = ct + div
            dif = val - n
            k = div - dif
            number = i
            ct = n + 1
        i += 1
    return [number, k]
def n_th(a):
    ct=0
    if(a[0]==1):
        return 1
    else:
        for i in range(2,a[0]+1):
            if(a[0]%i==0 and prime_nr(i)==1):
                ct+=1
                if(ct==a[1]):
                    return i
print("write a number")
nr= input()
nr=int(nr)
a = number_divisor(nr)
print("the",nr,"-th element of the sequence is:")
print(n_th(a))
    
