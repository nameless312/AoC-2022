def read_input():
	rucks = []
	with open("input.txt") as fp:
		for line in fp.readlines():
			line = line.strip()
			rucks.append(line)
	return rucks

def get_item_type(group):
	for l1 in group[0]:
		for l2 in group[1]:
			for l3 in group[2]:
				if l1 == l2 and l2 == l3:
					return l1

def calc_priorities(rucks):
	total = 0
	group = []
	for i, ruck in enumerate(rucks):
		group.append(ruck)
		if((i + 1) % 3 == 0):
			item_type = get_item_type(group)
			if 'a' <= item_type <= 'z':
				total += ord(item_type) - 96
			else:
				total += ord(item_type) - 64 + 26
			group.clear()		
	return total

def solve():
	rucks = read_input()
	print(calc_priorities(rucks))

if __name__ == "__main__":
	solve()