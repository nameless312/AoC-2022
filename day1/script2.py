def read_input():
	with open("input.txt") as fp:
		return fp.readlines()

def calculate_cals(source):
	cals = []
	elf_idx = 0
	for line in source:
		if line == "\n":
			elf_idx += 1
		else:
			if elf_idx + 1 > len(cals):
				cals.insert(elf_idx, int(line))
			else:
				cals[elf_idx] = cals[elf_idx] + int(line)
	return cals

def solve():
	source = read_input()
	elf_calories = calculate_cals(source)
	elf_calories.sort(reverse=True)
	total = 0
	for i in range(3):
		total += elf_calories[i]
	print(f"Top 3 cals -> {total}")
	
if __name__ == "__main__":
	solve()