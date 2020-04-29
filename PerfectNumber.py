num, nums = int(input("numer to test : ")), []

for i in range(1, num):
	if num%i == 0:
		nums +=[i]
resu = sum(nums)
if resu == num and num != 0:
	print(f"{num} is perfect")
else:
	print(f"{num} is not perfect")
	