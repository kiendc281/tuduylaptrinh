#kiemtrasochinhphuong
a=int(input('nhap so can kiem tra: '))
kq=0
while (a<0):
    print('Khong phu hop! Vui long nhap lai')
    a = int(input('nhap so'))
if (a==0):
    print(a,'la so chinh phuong')
elif (a==1):
    print(a, 'la so chinh phuong')
else:
    for i in range(1,a+1):
        import math
        if math.sqrt(a)%1==0:
            kq=1
        else:
            kq=2
if kq==1:
    print(a,'la so chinh phuong')
if kq==2:
    print(a,'khong la so chinh phuong')

