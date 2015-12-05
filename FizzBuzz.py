count = 0

while count < 100:
	count  = count + 1
	current = count
	if (current %3 == 0) and (current %5 == 0):
		print("FizzBuzz")
		continue

	if current %3 == 0:
		print("Fizz")
		continue

	if current %5 == 0:
		print("Buzz")
		continue

	print(current)