#tim uoc chung lon nhat cua 2 so
a=int(input('nhap a: '))
b=int(input('nhap b: '))
for i in range(1,a+1):
    if (a%i==0) and (b%i==0):
        uc=i
print('uoc chung lon nhat cua a,b la',uc)