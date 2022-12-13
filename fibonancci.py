#tim so hang thu n cua day fibonancci
#fn=f(n-1)+f(n-2)
n=int(input('nhap so hang'))
f0=0
f1=1
f2=1
fn=1
if (n==0):
    print('0')
elif (n==1) or (n==2):
    print('so hang thu',n,'trong day fibonancci la 1')
elif(n>2):
    for i in range(2,n):
        f0=f1
        f1=fn
        fn=f0+f1
    print('so hang thu',n,'trong day fibonacci la',fn)
else:
    print('khong hop le')