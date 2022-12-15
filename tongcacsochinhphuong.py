#tong cac so chinh phuong tu 1 --> a
#kiemtrasochinhphuong
a=int(input('nhap so: '))
tong=0
for i in range(1,a+1):
    import math
    if math.sqrt(i)%1==0:
        tong=tong+i
print(tong)