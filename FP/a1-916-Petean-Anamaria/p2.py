# Solve the problem from the second set here
#Consider a given natural number n.
#Determine the product p of all the proper factors of n.
def product(nr):
    p=1
    for i in range(2,nr):
        if(nr%i==0):
            p=p*i
    return p
print("write a number:")
nr= input()
nr=int(nr)
print("the product of all the proper factors of ",nr," is:")
print(product(nr))
