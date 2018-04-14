import random
import sys

def generate_unique_numbers():
	x = 0
	rand_list = []
	seen = set()
	while x < 7:
		rand = random.randint(1,40)
		if rand not in seen:
			rand_list.append(rand)
			seen.add(rand)
			x = x + 1
	rand_list.sort()
	return rand_list;

def check_right(my_numbers, random_numbers):
	correct = 0
	for number in my_numbers:
		for num in random_numbers:
			if number == num:
				correct = correct + 1
				break
	return correct;

my_list = [3, 6, 16, 18, 27, 35, 39]
best = 0
i = 0
while i < sys.maxsize:
	i = i + 1
	rnd_list = generate_unique_numbers()
	corr = check_right(my_list, rnd_list)
	if corr > best:
		print("{0:2d} {1:12d}".format(corr,i))
		best = corr
	if corr == 7:
		i = 0
		best = 0
