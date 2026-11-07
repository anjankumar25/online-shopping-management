def items(a,b):

    def kart(c,d):
        nonlocal a,b
        if a>=c:
            a=a-c
            print("the requsted items ",c)
            h=500
            i=c*h
            print(f"the coast of {c} shoes ",i)
            
        elif a<c:
            print("error")
            
        
        if b>=d:
            b=b-d
            print("the requsted items ",d)
            hi=300
            ii=d*hi
            print(f"the coast of {d} shirts ",ii)
            
        elif b<d:
            print("error")
        hp=hi+i
        print("the amount is ",hp)
        if hp>=2000:
            hpp=hp/10
            vpp=hp-hpp
            print("the amount after discount",vpp)
        else:
            print("the amount",hpp)
        return a,b

            
        

    order=kart(12,11)
    print("the ordered items ",order)
rem=items(25,25)

print("the remaining itmes",rem)
