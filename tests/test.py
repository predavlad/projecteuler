n=raw_input().split(',');a=int(n[0]);b=int(n[1])
f=lambda n:n<2and 1or n*f(n-1)
print f(a)/f(b)/f(a-b)
