#increasing ordered tables
#this is the smallest way to write code in for loop only.


a =int(input('enter your number'))
for b in range(1,a+1,1):
	for i in range(1,11,1): print(b,'*',i,'=',b*i)
	print()	