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
		if int(pair[0][0]) <= int(pair[1][0]) and int(pair[0][1]) >= int(pair[1][1]):
			overlaps += 1
		elif int(pair[1][0]) <= int(pair[0][0]) and int(pair[1][1]) >= int(pair[0][1]):
			overlaps += 1
	return overlaps

def solve():
	pairs = read_input()
	print(calc_overlaps(pairs))

if __name__ == "__main__":
	solve()