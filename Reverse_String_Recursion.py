def rev_str(s):
    if len(s)<=1:
        return s
    else:
        return s[-1]+rev_str(s[:-1])
str1=input("Enter a string: ")
print(rev_str(str1))
