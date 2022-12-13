def fibo(n):
    f0=0
    f1=1
    f2=1
    fn=1
    if(n==0):
        return -1
    elif (n==1) or (n==2):
        return 1
    elif (n>2):
        f0=f1
        f1=fn
        fn=f0+f1
        return fn
    print(fn)
fibo(10)
print(fibo(10))
