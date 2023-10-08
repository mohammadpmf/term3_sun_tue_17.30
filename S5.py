def add(a=0, b=0, c=0,d=0, *args, **kwargs):
    print(args)
    print(kwargs)
    return a+b+c+d

print(add(7,8))
print(add(7,8,9,4,8,7,5,3,2,4,5,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4, w=5, kk='red', bg='blue'))
print(add(17,8,1))