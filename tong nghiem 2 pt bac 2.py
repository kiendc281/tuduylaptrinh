#tong nghiem 2 pt bac 2 dang ax^2+bx+c=0 va dx^2+ex+f=0 khi co 2 nghiem
a = float(input('nhap a'))
b = float(input('nhap b'))
c = float(input('nhap c'))
while (a==0):
    print('phuong trinh khong hop le! Vui long nhap lai')
    a = float(input('nhap a'))
    b = float(input('nhap b'))
    c = float(input('nhap c'))
print('phuong trinh thu nhat co dang',a,'x^2 +',b,'x +',c,'=0')
d = float(input('nhap d'))
e = float(input('nhap e'))
f = float(input('nhap f'))
while(d==0):
    print('phuong trinh khong hop le! Vui long nhap lai')
    d = float(input('nhap d'))
    e = float(input('nhap e'))
    f = float(input('nhap f'))
print('phuong trinh thu hai co dang',d,'x^2 +',e,'x +',f,'=0')
print('')
d1=b**2-4*a*c
d2=e**2-4*d*f
t=0
t1=0
t2=0
if(d1>0):
    t1=-b/a
    print('tong hai nghiem cua phuong trinh thu nhat la:',t1)
else:
    print('phuong trinh thu nhat co it hon 2 nghiem')
    t1=0
if(d2>0):
    t2=-e/d
    print('tong hai nghiem cua phuong trinh thu hai la:',t2)
else:
    print('phuong trinh co it hon 2 nghiem')
    t2=0
t=t1+t2
print('tong hai nghiem cua 2 phuong trinh la: ',t)