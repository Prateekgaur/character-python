#code
n = int(input())
j = 1
for i in range(n):
    if i < n//2+1:
        print( (n//2+i)*'*' +' '*(n-2*i) + (n//2+i)*'*')
    else:
        print( (n//2)*'*' +' '*(j)+ '*'*(n-2*(j)) +' '*(j)+(n//2)*'*')
        j += 1
