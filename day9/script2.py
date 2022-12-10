def read_input():
	ops = []
	with open("example.txt") as fp:
		for line in fp.readlines():
			line = line.strip().split(' ')
			ops.append((line[0], int(line[1])))
	return ops

def get_new_t(xT,yT,xH,yH):
	new_xT = xT
	new_yT = yT
	# up
	if yH - yT == 2:
		# diag up right
		if xH - xT == 1:
			new_xT += 1
			new_yT += 1
		# diag up left
		elif xT - xH == 1:
			new_xT -= 1
			new_yT += 1
		else:
			new_yT += 1
	# right
	elif xH - xT == 2:
		# diag up right
		if yH - yT == 1:
			new_xT += 1
			new_yT += 1
		# diag down right
		elif yT - yH == 1:
			new_xT += 1
			new_yT -= 1
		else:
			new_xT += 1
	# bottom
	elif yT - yH == 2:
		# diag bottom right
		if xH - xT == 1:
			new_xT += 1
			new_yT -= 1
		# diag bottom left
		elif xT - xH == 1:
			new_xT -= 1
			new_yT -= 1
		else:
			new_yT -= 1
	# left
	elif xT - xH == 2:
		# diag top left
		if yH - yT == 1:
			new_xT -= 1
			new_yT += 1
		# diag bottom left
		elif yT - yH == 1:
			new_xT -= 1
			new_yT -= 1
		else:
			new_xT -= 1
	return (new_xT, new_yT)

def iter_ops(ops):
	tail_coords = set()
	rope = [(0,0)] * 9
	xH = 0
	yH = 0
	tail_coords.add(rope[8])
	for op in ops:
		for i in range(op[1]):
			if op[0] == 'U':
				yH += 1
			elif op[0] == 'R':
				xH += 1
			elif op[0] == 'D':
				yH -= 1
			else:
				xH -= 1

			rope[0] = get_new_t(rope[0][0],rope[0][1],xH,yH)
			for i in range(len(rope))[1:]:
				rope[i] = get_new_t(rope[i][0],rope[i][1],rope[i - 1][0],rope[i - 1][1])
			tail_coords.add(rope[8])
	return len(tail_coords)	
			
def solve():
	ops = read_input()
	unique_coords = iter_ops(ops)
	print(unique_coords)

if __name__ == "__main__":
	solve()