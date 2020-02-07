#num in 1-100
#while num%7 equal 0 or num%10 equal 7 or num/10 equal7
#then no print num 
for num in range(1,101):
	if(num%7==0 or num%10==7 or int(num/10)==7):
		continue
	else:
		print(num)
