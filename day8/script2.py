def read_input():
	grid = []
	with open("input.txt") as fp:
		for row in fp.readlines():
			row = [x for x in row.strip()]
			grid.append(row)
	return grid

def get_visible_trees(grid):
	size = range(1,len(grid) - 1)
	max_score = 0
	for i in size:
		for j in size:
			left = []
			right = []
			top = []
			bottom = []
			score = 0

			# left
			for z in reversed(range(j)):
				left.append(grid[i][z])
				if grid[i][j] <= grid[i][z]:
					break
			# right
			for z in range(j + 1,len(grid)):
				right.append(grid[i][z])
				if grid[i][j] <= grid[i][z]:
					break
			# top
			for z in reversed(range(i)):
				top.append(grid[z][j])
				if grid[i][j] <= grid[z][j]:
					break
			# bottom
			for z in range(i + 1,len(grid)):
				bottom.append(grid[z][j])
				if grid[i][j] <= grid[z][j]:
					break	

			score = len(right) * len(left) * len(top) * len(bottom)
			if score > max_score:
				max_score = score

	return max_score


def solve():
	grid = read_input()
	max_score = get_visible_trees(grid)
	print(max_score)

if __name__ == "__main__":
	solve()