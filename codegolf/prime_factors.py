i=1;r='';n=m=raw_input();n=int(n)
while n>1:
 c=0;i+=1
 while n%i==0:n/=i;c+=1
 if c:r+=' '+str(i)
 if c>1:r+='^'+str(c)
print m+':'+r
