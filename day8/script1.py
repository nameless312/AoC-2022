def read_input():
	grid = []
	with open("input.txt") as fp:
		for row in fp.readlines():
			row = [x for x in row.strip()]
			grid.append(row)
	return grid

def get_visible_trees(grid):
	size = range(1,len(grid) - 1)
	hidden_trees = 0
	for i in size:
		for j in size:
			left = []
			right = []
			top = []
			bottom = []

			# left
			for z in range(j):
				left.append(grid[i][z])
			# right
			for z in range(j + 1,len(grid)):
				right.append(grid[i][z])

			# top
			for z in range(i):
				top.append(grid[z][j])

			# bottom
			for z in range(i + 1,len(grid)):
				bottom.append(grid[z][j])

			if max(left) >= grid[i][j] and max(right) >= grid[i][j] and max(top) >= grid[i][j] and max(bottom) >= grid[i][j]:
				hidden_trees += 1
	return (len(grid) ** 2) - hidden_trees


def solve():
	grid = read_input()
	visible_trees = get_visible_trees(grid)
	print(visible_trees)

if __name__ == "__main__":
	solve()