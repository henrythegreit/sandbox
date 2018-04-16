import random
import sys
from collections import defaultdict

def generate_lotto_numbers():
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

number_stats = defaultdict(int)
j = 0
i = 0
#while i < sys.maxsize:
while i < sys.maxsize:
	i = i + 1
	rnd_list = generate_lotto_numbers()
	for numb in rnd_list:
		number_stats[numb] += 1


for k, v in number_stats.items():
	print(k,v)