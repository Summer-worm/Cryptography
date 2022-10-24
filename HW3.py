def fastPower(a,n,m):
    amutiplier=1
    list=[]
    while n!=0:       #that is the part from getBinaryExpansion(b), it is easier to solve the problem, so I use a part of it.
        n0=n%2
        n=int((n-n0)/2)
        list.append(n0)
    for x in list:
        if x==0:
            amodulo=a%m
            a=(amodulo*amodulo)%m
        else:
            amodulo=a%m
            a=(amodulo*amodulo)%m
            amutiplier=(amutiplier*amodulo)%m
    return amutiplier

def multInverse(a,p):
    # use p0 to save the ordinary prime
    p0=p
    b=a%p
    list3=[]
    s0=1
    s1=0
    t0=0
    t1=1
    while p%b!=0:
        r1=p%b
        q=p//b
        s2=s0-(q*s1)
        s0=s1
        s1=s2
        t2=t0-(q*t1)
        t0=t1
        t1=t2
        p=b
        b=r1
    list3=[b,s1,t1]
    # the value of a*t1 modulo p is -1, so we need to add ordinary p0
    return (p0+t1)%p0

def babyGiant(g,h,p,N):
    n=int(pow(N,0.5))+1
    list1=[1]
    list2=[h]
    counting=0
    orgin_g1=1
    orgin_g2=h
    while counting<n:
        orgin_g1=(orgin_g1*g)%p
        list1.append(orgin_g1)
        counting=counting+1
    gn=list1[-1]
    inv_gn=multInverse(gn,p)
    counting=0
    #A new loop begins,so counting will be 0 again
    while counting<n:
        orgin_g2=(orgin_g2*inv_gn)%p
        list2.append(orgin_g2)
        counting=counting+1
    i=0
    j=0
    list_answer=[]
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                return i+j*n
                j=j+1
            else:
                continue
        i=i+1
    return list_answer

def CRT(rList,mList):
    #First we need to build multiplier M
    j=0
    M=1
    for j in range(len(mList)):
        M=M*mList[j]
    j=0 #Another loop begins, j should be initialed
    listMj=[]
    while j<len(mList):
        a=int(M/mList[j])
        listMj.append(a)
        j=j+1
    inv_listMj=[]
    j=0 #Another loop begins, j should be initialed
    while j<len(mList):
        inv=multInverse(listMj[j],mList[j])
        inv_listMj.append(inv)
        j=j+1
    summ=0
    j=0 #Another loop begins, j should be initialed
    while j<len(mList):
        summ=summ+rList[j]*listMj[j]*inv_listMj[j]
        j=j+1
    solution=summ%M
    return solution

def pohligHellman(g,h,p,orderFactors):
    i=0
    list_power=[]
    for i in range(len(orderFactors)):
        a=(p-1)//orderFactors[i]
        list_power.append(a)
    i=0
    list_gpower=[]
    list_hpower=[]
    while i < len(orderFactors):
        g1=fastPower(g,list_power[i],p)
        h1=fastPower(h,list_power[i],p)
        list_gpower.append(g1)
        list_hpower.append(h1)
        i=i+1
    i=0
    list_CRT=[]
    while i < len(orderFactors):
        power2=babyGiant(list_gpower[i],list_hpower[i],p,p-1)
        list_CRT.append(power2)
        i=i+1
    print(CRT(list_CRT,orderFactors))
p = 2189248127867
g = 1267362
h = 1244880003213
orderFactors=[2,29,2459,15350003]
pohligHellman(g,h,p,orderFactors)