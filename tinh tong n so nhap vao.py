#nhap vao n so, tinh tong tat ca cac so do
n=int(input('ban muon tinh tong bao nhieu so: '))
s=0
t=0
for i in range(1,n+1):
    a=int(input('nhap so: '))
    s=s+a
t=t+s
print('tong cac so la:',t)