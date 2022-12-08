def read_input():
	with open("input.txt") as fp:
		fs = {}
		fs["/"] = {"tp":"dir","children":dict(),"parent":dict(),"size":0}
		curr_dir = ["/"]
		curr_tree = fs["/"]
		for i,line in enumerate(fp.readlines()):
			if i != 0:
				line = line.strip()
				if line.startswith("$"):
					command = line.split(" ")
					if command[1] == "cd":
						if command[2] != "..":
							curr_dir.append(command[2])
							curr_tree = curr_tree.get("children")[command[2]]
						else:
							curr_dir.pop()
							curr_tree = curr_tree.get("parent")
				else:
					if line.startswith("dir"):
						directory = line.split(" ")
						curr_tree.get("children")[directory[1]] = {"tp":"dir","children":dict(),"parent":curr_tree,"size":0}
					else:
						file = line.split(" ")
						curr_tree.get("children")[file[1]] = {"tp":"file","size":int(file[0])}
		update_dir_sizes(fs["/"])
		return fs

def update_dir_sizes(curr_dir):
	children = curr_dir.get("children")
	for child in children.values():
		if child.get("tp") == "dir":
			if child.get("children"):
				update_dir_sizes(child)
			curr_dir["size"] += int(child["size"])
		else:
			curr_dir["size"] += int(child["size"])
	return curr_dir


def get_dirs_size(curr_dir, sizes, available_space):
	if available_space + curr_dir.get("size") >= 30_000_000:
		sizes.append(curr_dir.get("size"))

	children = curr_dir.get("children")
	for child in children.values():
		if child.get("tp") == "dir":
			if child.get("children"):
				get_dirs_size(child, sizes,available_space)
	return sizes

def solve():
	fs = read_input()
	available_space = 70_000_000 - fs["/"].get("size")
	size = min(get_dirs_size(fs.get("/"), [], available_space))
	print(size)

if __name__ == "__main__":
	solve()