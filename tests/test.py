i=2;r='';n=m=raw_input();n=int(n)
while n>1:
 c=0
 while n%i==0:n/=i;c+=1
 if c:r+=' '+str(i)
 if c>1:r+='^'+str(c)
 i+=1
print m+':'+r
