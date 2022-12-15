#kiemtrasochinhphuong
a=int(input('nhap so'))
kq=0
while a<0:
    print('vui long nhap lai')
if (a==0):
    print(a,'la so chinh phuong')
elif (a==1):
    print(a,'la so chinh phuong')
else:
    for i in range(1,a+1):
        if ((i**2)==a):
            kq=1
    if (kq==1):
        print(a,'la so chinh phuong')
    else:
        print(a,'khong la so chinh phuong')