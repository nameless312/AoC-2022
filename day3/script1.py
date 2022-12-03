def read_input():
	rucks = []
	with open("input.txt") as fp:
		for line in fp.readlines():
			line = line.strip()
			comp1,comp2 = line[:len(line)//2], line[len(line)//2:]
			rucks.append((comp1,comp2))
	return rucks

def get_item_type(comp1, comp2):
	for i in range(len(comp1)):
		for j in range(len(comp2)):
			if comp1[i] == comp2[j]:
				return comp1[i]

def calc_priorities(rucks):
	total = 0
	for ruck in rucks:
		item_type = get_item_type(ruck[0], ruck[1])
		if 'a' <= item_type <= 'z':
			total += ord(item_type) - 96
		else:
			total += ord(item_type) - 64 + 26
	return total

def solve():
	rucks = read_input()
	print(calc_priorities(rucks))

if __name__ == "__main__":
	solve()