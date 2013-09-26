s=["%d bottle%s of beer","on the wall","Take one down and pass it around","Go to the store and buy some more"];i=99;t=['s']*101;t[1]='';b='.\n'
while i:a=s[0]%(i,t[i]);print a,s[1]+',',a+b+(s[3],s[2])[i>1]+",",s[0]%((i-1,99)[i<2],t[i-1]),s[1]+b;i-=1
