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
	print(f"Most cals -> {max(elf_calories)}")
	
if __name__ == "__main__":
	solve()