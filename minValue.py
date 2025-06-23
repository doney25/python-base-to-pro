a=list(map(int,input('Enter some numbers:').split()))
minvalue=a[0]

for i in a:
    if i<minvalue:
        minvalue=i
    
print(f'Minimum Value is {minvalue}')        