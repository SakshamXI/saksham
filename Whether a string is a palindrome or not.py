a = str(input(" "))
n =0
b = (len(a)-1)//2
for i in range(b):
    if a[i] == a[-(i+1)]:
        n = n+1
if n == b:
    print('Yes,it is a palindrome')
else:
    print('No,it is not a palindrome')

    
        

    

    
    