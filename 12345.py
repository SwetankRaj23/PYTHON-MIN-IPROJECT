def fun(a,b) :
    if b=="INR" :
        a=a
    elif b=="USD" :
        a*=80
    elif b=="canadian dollar" :
        a*=62
    elif b=="chinese yuan" :
        a*=12
    elif b=="russian ruble" :
        a*=(1.4)
    elif b=="pounds" :
        a*=(4.2)
    elif b=="euros" :
        a*=(81.4) 
    return(a)
def fun2(x,c) :
    if c=="INR" :
        x=x
    elif c=="USD" :
        x/=80
    elif c=="canadian dollar" :
        x/=62
    elif c=="chinese yuan" :
        x/=12
    elif c=="russian ruble" :
        x/=(1.4)
    elif c=="pounds" :
        x/=(4.2)
    elif c=="euros" :
        x/=(81.4) 
    return(x)
a=float(input("Amount: "))
print("Chose from the given currencies")
b=input("Currency(INR,USD,canadian dollar,chinese yuan,russian ruble,pounds,euros) :")
c=input("Currency to be converted in(INR,USD,canadian dollar,chinese yuan,russian ruble,pounds,euros) :")
x=fun(a,b)
z=fun2(x,c)
print(z,c)
