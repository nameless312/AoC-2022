def read_input():
	choices = []
	with open("input.txt") as fp:
		for line in fp.readlines():
			line = line.strip().split(" ")
			choice = (line[0],line[1])
			choices.append(choice)
		return choices

def calculate_score(choice):
	score = 0
	# A | X -> Rock
	# B | Y -> Paper
	# C | Z -> Scissor
	if (choice[1] == 'X' and choice[0] == 'C' 
		or choice[1] == 'Y' and choice[0] == 'A' 
		or choice[1] == 'Z' and choice[0] == 'B'):
		score += 6
	elif (choice[1] == 'X' and choice[0] == 'A' 
		or choice[1] == 'Y' and choice[0] == 'B' 
		or choice[1] == 'Z' and choice[0] == 'C'):
		score += 3

	if choice[1] == 'Z':
		score += 3
	elif choice[1] == 'Y':
		score += 2
	else:
		score += 1
	return score

def solve():
	choices = read_input()
	total_score = 0
	for choice in choices:
		total_score += calculate_score(choice)
	print(total_score)

if __name__ == "__main__":
	solve()