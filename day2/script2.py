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
	# A -> Rock    (1)	Y -> Draw (3)
	# B -> Paper   (2)	X -> Lose (0)
	# C -> Scissor (3)	Z -> Win (6)
	
	if choice[0] == 'A':
		if choice[1] == 'Z':
			score += 6
			score += 2
		elif choice[1] == 'Y':
			score += 3
			score += 1
		else:
			score += 3


	elif choice[0] == 'B':
		if choice[1] == 'Z':
			score += 6
			score += 3
		elif choice[1] == 'Y':
			score += 3
			score += 2
		else:
			score += 1

	if choice[0] == 'C':
		if choice[1] == 'Z':
			score += 6
			score += 1
		elif choice[1] == 'Y':
			score += 3
			score += 3
		else:
			score += 2
	return score

def solve():
	choices = read_input()
	total_score = 0
	for choice in choices:
		total_score += calculate_score(choice)
	print(total_score)

if __name__ == "__main__":
	solve()