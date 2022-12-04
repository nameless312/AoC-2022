def read_input():
	pairs = []
	with open("input.txt") as fp:
		for line in fp.readlines():
			line = line.strip().split(',')
			pairs.append((line[0].split('-'), line[1].split('-')))
	return pairs

def calc_overlaps(pairs):
	overlaps = 0
	for pair in pairs:
		p1 = set()
		p2 = set()
		for i in range(int(pair[0][1]) - int(pair[0][0]) + 1):
			p1.add(int(pair[0][0]) + i)
		for i in range(int(pair[1][1]) - int(pair[1][0]) + 1):
			p2.add(int(pair[1][0]) + i)
		if len(p1.intersection(p2)) > 0:
			overlaps += 1
	return overlaps

def solve():
	pairs = read_input()
	print(calc_overlaps(pairs))

if __name__ == "__main__":
	solve()