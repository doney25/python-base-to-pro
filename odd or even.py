#method1
import random
a=random.randrange(1,100)
if int(a)%2==0:
    print(f'{a} is even')
else:
    print(f"{a} is odd")

#method2
a=input('Enter the number: ')
print(f'{a} is even') if int(a)%2==0 else print(f'{a} is odd')
