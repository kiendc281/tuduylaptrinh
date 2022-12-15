#kiemtrasohoanhao
a=int(input('nhap so'))
s=0
#timuoc
for i in range(1,a):
    if a%i==0:
        s=s+i
if (s==a):
    print(a,'la so hoan hao')
else:
    print(a,'khong la so hoan hao')
