


import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

count = 0
ingredients = []
n = int(lines[0])
for i in range(1, n+1):
	t = lines[i].split()
	for j in t:
		if j not in ingredients:
			count += 1
			ingredients.append(j)
print(count)