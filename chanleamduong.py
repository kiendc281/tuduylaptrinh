a=int(input('nhap so can kiem tra: '))
if (a>0):
    if (a%2==0):
        print(a,'la so chan, duong')
    else:
        print(a,'la so le, duong')
elif (a<0):
    if (a % 2 == 0):
        print(a, 'la so chan, am')
    else:
        print(a, 'la so le, am')
else:
    print(a,'la so chan, khong am khong duong')