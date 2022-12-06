def read_input():
    with open("example.txt") as fp:
        return fp.read().strip()

def process(packets):
    curr = 0
    while curr + 4 <= len(packets):
        temp = []
        for i in range(4):
            if packets[curr + i] in temp:
                break
            else:
                temp.append(packets[curr + i])
            if len(temp) == 4:
                return curr + 4
        curr += 1

def solve():
    packets = read_input()
    print(process(packets))

if __name__ == "__main__":
    solve()