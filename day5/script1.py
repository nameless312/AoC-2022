def read_input():
	with open("example.txt") as fp:
		lines = fp.readlines()
		row = list(lines[0])
		size = len(row) // 4
		matrix = [[] for _ in range(size)]
		ops = []
		for line in lines:
			if not line.startswith('\n') and not line.startswith('move') and not line.startswith(' 1'):
				row = list(line)
				i = 1
				for j in range(size):
					if row[i] != ' ':
						matrix[j].insert(0,row[i])
					i += 4
			elif line.startswith('move'):
				op = []
				line = line.strip().split(" ")
				ops.append((int(line[1]),int(line[3]),int(line[5])))
		return matrix, ops

def iterate_ops(matrix,ops):

	for (q, pos1, pos2) in ops:
		for i in range(q):
			el = matrix[pos1-1].pop()
			matrix[pos2-1].append(el)
	return "".join([x[len(x) - 1] for x in matrix])

def solve():
	matrix, ops = read_input()
	res = iterate_ops(matrix, ops)
	print(res)

if __name__ == "__main__":
	solve()