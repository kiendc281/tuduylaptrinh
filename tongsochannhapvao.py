n=int(input('nhap so luong so muon tinh: '))
s=0
for i in range(1,n+1):
    a=int(input('nhap so'))
    if(a%2==0):
        s=s+a
print('tong cac so chan la',s)
