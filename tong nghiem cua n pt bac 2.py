#tong nghiem cua n pt bac 2 neu co nghiem kep
n=int(input('nhap so phuong trinh muon tinh'))
t=0
for i in range(1,n+1):
    a = float(input('nhap a'))
    b = float(input('nhap b'))
    c = float(input('nhap c'))
    while(a==0):
        print('nhap sai! Vui long nhap lai')
        a = float(input('nhap a'))
        b = float(input('nhap b'))
        c = float(input('nhap c'))
    print('phuong trinh thu',i,'co dang',a,'x^2 +',b,'x +',c,'=0')
    d=b**2-4*a*c
    if(d==0):
        print('phuong trinh co nghiem kep')
        nk=-b/a
        print('gia tri nghiem kep la:',nk)
        t=t+nk
    else:
        print('phuong trinh khong co nghiem khep')
print('tong nghiem cua phuong trinh khi co nghiem kep la',t)