def ftest(x):
    a=[]
    for i in x:
        q=0
        for j in x:
            if j == i :
                q+=1
            if q >1 :
                break
        if q > 1 :
            pass
        else:
            a.append(i)
    return a
x=input()
print(ftest(x))