import random
import sys
from collections import defaultdict
import operator
import matplotlib.pyplot as plt

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
i = 0
amount = 1000000
while i < amount:
	i = i + 1
	rnd_list = generate_lotto_numbers()
	for numb in rnd_list:
		number_stats[numb] += 1
plt.plot(number_stats.keys(), number_stats.values())
print("Num     Count      %")
print("--------------------")
for w in sorted(number_stats, key=number_stats.get, reverse=True):
	value = (float(number_stats[w]) / float(amount)) * 100.0
	print("{0:2d} {1:10d}  {2:4.2f}".format(w, number_stats[w], value))
	if(i == 0):
		break;
plt.show()
