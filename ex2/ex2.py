import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

n, m = map(int, lines[0].split())
pizz = [list(map(int, lines[i].split())) for i in range(1, n+1)]
res = 0
for order_i in lines[n+1: n+1+m]:
    x, y = map(int, order_i.split())
    best = float('inf')
    for xp, yp in pizz:
        dst = abs(xp-x) + abs(yp-y)
        best = min(best, dst)
    res += best
print(2*res) # Account for all return trips